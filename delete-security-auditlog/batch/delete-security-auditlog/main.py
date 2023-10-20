import os
from datetime import datetime

from opensearchpy import OpenSearch
from authentication import authentication as auth
import logging


def _parse_date(index_name: str) -> datetime:
    """
    Parses date out of security-auditlog-index

    :param index_name: the index-name
    :return: date of security-auditlog-index
    """
    return datetime.strptime(index_name.replace('security-auditlog-', ''), '%Y.%m.%d')


def _list_deleteable_indices(client: OpenSearch) -> list:
    """
    List all security-auditlog-indices that can be deleted, keep a configured number of most recent indices
    :param client: the opensearch-client
    :return: list of security-auditlog-indices that can be deleted
    """
    auditlogs = client.cat.indices(index='security-auditlog-*', h='index').split()
    indices2keep = int(os.environ['INDICES_TO_KEEP'])

    date2index = {_parse_date(index): index for index in auditlogs}
    dates = list(date2index.keys())
    dates.sort()
    indices2delete = dates[:-indices2keep]

    return [index for date, index in date2index.items() if date in indices2delete]


def _delete_index(client: OpenSearch, index_name: str):
    """
    Deletes the given index
    :param client: the opensearch-client
    :param index_name: the name of the index
    """
    logging.info(f'deleting index {index_name}')
    client.indices.delete(index=index_name)


if __name__ == '__main__':
    FORMAT = '%(asctime)s %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)

    opensearchUrl = os.environ['OPENSEARCH_URL']
    access_token = auth.TokenHolder().get_access_token()['access_token']
    client = OpenSearch([opensearchUrl], use_ssl=True, verify_certs=False,
                        headers={"Authorization": f'Bearer {access_token}'})

    deleteables = _list_deleteable_indices(client)
    [_delete_index(client, d) for d in deleteables]

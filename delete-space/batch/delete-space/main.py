import logging
import os
from datetime import datetime

from authentication import authentication as auth
from organizationmanager import organizationmanager


def _should_be_deleted(space: dict) -> bool:
    try:
        # check for 'state' key
        if 'state' not in space:
            logging.info('key "state" not in space - inconsistent data!')
            return False

        # check for 'modified' key
        if space['state'] == 'DELETION' and ('modified' not in space or space['modified'] is None):
            logging.info(f'space {space["name"]} marked for deletion but "modified" not set - inconsistent data!')
            return False

        # check if state is 'deletion' and if time since modification is at least 7 days
        return (
                space['state'] == 'DELETION' and
                (datetime.now() - datetime.fromtimestamp(space['modified'])).days >= 7
        )
    except Exception as e:
        logging.info(f'unexpected error occurred: {e}')
        return False


if __name__ == '__main__':
    FORMAT = '%(asctime)s %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)

    # Getting configuration and initializing client
    org_manager_url = os.environ.get('ORGANIZATIONMANAGER_URL')
    access_token = auth.TokenHolder().get_access_token()['access_token']
    org_manager_client = organizationmanager.OrganizationManagerClient(org_manager_url, access_token)

    # Fetch organizations and filter spaces that have to be deleted for all organizations
    logging.info('getting organizations...')
    organizations = org_manager_client.get_organizations()
    logging.info('getting spaces to be deleted...')
    orgs_with_spaces_to_be_deleted = [
        {
            'id': org['id'],
            'name': org['name'],
            'spaces': [space for space in org_manager_client.get_spaces(org['id']) if _should_be_deleted(space)]
        }
        for org in organizations
    ]

    # Delete spaces and log the operations
    delete_cnt = 0
    for org in orgs_with_spaces_to_be_deleted:
        for space in org['spaces']:
            logging.info(f'deleting space {space.get("name", "space without name - this should never happen!!")}...')
            org_manager_client.delete_space(org['id'], space['id'])
            delete_cnt += 1

    logging.info(f'{delete_cnt} spaces deleted.')

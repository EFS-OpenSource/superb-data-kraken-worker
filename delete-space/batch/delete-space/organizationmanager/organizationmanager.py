from typing import List, Dict

import requests


class OrganizationManagerClient:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_organizations(self) -> List[Dict]:
        url = f'{self.url}/organization'
        headers = {
            'Authorization': f'Bearer {self.token}',
            'accept': 'application/json'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

    def get_spaces(self, organization_id: int):
        url = f'{self.url}/space/{organization_id}'
        headers = {
            'Authorization': f'Bearer {self.token}',
            'accept': 'application/json'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

    def delete_space(self, organization_id: int, space_id):
        url = f'{self.url}/space/{organization_id}/{space_id}'
        headers = {
            'Authorization': f'Bearer {self.token}',
            'accept': 'application/json'
        }

        response = requests.delete(url, headers=headers)
        response.raise_for_status()

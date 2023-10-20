# -*- encoding: utf-8 -*-
import logging
import os
from datetime import datetime, timedelta

import requests


class TokenHolder:
    """
    Object to hold and refresh access-tokens
    """

    def __init__(self):
        auth_header = self._get_service_account_access_token()
        self.token = auth_header['token']
        self.generated_at = auth_header['generated_at']

    def _get_service_account_access_token(self):
        """
        Generates OAuth-Token for the service account
        :return: expires-in and access-token
        """

        logging.info("getting access-token")
        access_token_uri = os.environ['ACCESS_TOKEN_URI']
        client_id = os.environ['CLIENT_ID']
        client_secret = os.environ['CLIENT_SECRET']

        payload = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.post(access_token_uri, headers=headers, data=payload)
        response.raise_for_status()

        logging.info("got service account access-token")

        self.token = response.json()

        return {'token': self.token, 'generated_at': datetime.now()}

    def _refresh_access_token(self):
        """
        Refreshes the OAuth-Token for the given user
        :return: token
        """
        logging.info("refreshing access-token")
        access_token_uri = os.environ['ACCESS_TOKEN_URI']
        client_id = os.environ['CLIENT_ID']

        payload = f'grant_type=refresh_token&refresh_token={self.token["refresh_token"]}&client_id={client_id}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.post(access_token_uri, headers=headers, data=payload)
        response.raise_for_status()

        logging.info("access-token refreshed")

        return response.json()

    def get_access_token(self):
        """
        Gets a valid access-token (either stored, refreshed or new token)

        Returns
        -------
        [dict]
            valid access-token
        """
        expires_in = self.token['expires_in']
        token_expiration = self.generated_at + timedelta(seconds=expires_in)
        # check, if token is still valid
        if datetime.now() >= token_expiration:
            refresh_expiration = self.generated_at + timedelta(seconds=self.token['refresh_expires_in'])
            # check, if token-refresh is still possible
            if datetime.now() < refresh_expiration:
                # refresh the token
                self.token = self._refresh_access_token()
            else:
                # generate a new token
                auth_header = self._get_service_account_access_token()
                self.token = auth_header['token']
                self.generated_at = datetime.now()
        return self.token

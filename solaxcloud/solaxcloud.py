"""
Solax Cloud API Wrapper.
https://www.solaxcloud.com/proxyApp/proxy/api/getRealtimeInfo.do?tokenId=XXXXXXXXXXXXXXXXXXXXXXX&sn=XXXXXXXXXX
Add serial number for the Solax pocket lan or pocket wifi, NOT the inverter serial.
Add token from API page on solax cloud webpage.
"""

import requests
from requests.adapters import HTTPAdapter, Retry

__title__ = "Solax"
__version__ = "0.1.0"
__author__ = "Frank van der Heide, frankvanderheide89@gmail.com>"
__license__ = "MIT"

session = requests.Session()
retries = Retry(total=5, backoff_factor=0.2, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))


class solaxcloud:
    """Solax class."""

    baseurl = "https://www.solaxcloud.com/proxyApp/proxy/api/"

    def __init__(self, token: str, registration_number: str) -> None:
        """To get data from the cloud we need a API token and a registrion number(the number of the lan or wifi module)."""

        self.token = token.strip()
        self.registration_number = registration_number.strip()

    def validate_token_and_registration_number(self):
        """Check if the supplied token and serial number are valid."""
        url = self.baseurl + "getRealtimeInfo.do?"
        responce = session.get(
            url,
            timeout=1,
            params={"tokenId": self.token, "sn": self.registration_number},
        )

        responce.raise_for_status()
        solax_responce = responce.json()

        if solax_responce["success"] is True:
            return True
        else:
            return None

    def get_realtime_data(self):
        """Get realtime data from the cloud."""
        url = self.baseurl + "getRealtimeInfo.do?"
        responce = session.get(
            url,
            timeout=1,
            params={"tokenId": self.token, "sn": self.registration_number},
        )

        responce.raise_for_status()
        solax_responce = responce.json()

        if solax_responce["success"] is True:
            dictonary = solax_responce["result"]
            return dictonary
        else:
            return None

    def get_firmware_history(self):
        """Get firmware history."""
        url = self.baseurl + "upHistory?"
        responce = session.get(
            url,
            timeout=1,
            params={"tokenId": self.token, "sn": self.registration_number},
        )

        responce.raise_for_status()
        solax_responce = responce.json()

        if solax_responce["success"] is True:
            dictonary = solax_responce["result"]
            return dictonary
        else:
            return None

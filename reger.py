from utils import logger
import tls_client
import tls_client.sessions
from random import choice
from pyuseragents import random as random_useragent

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://referlist.co',
    'referer': 'https://referlist.co/',
    'user-agent': random_useragent()
}


class Reger:
    def __init__(self, mail: str):
        self.mail = mail

    def add_to_waitlist(self, ref_code: str, session: tls_client.sessions.Session) -> bool:
        url = "https://referlist.herokuapp.com/api/addtowaitlist"

        json = {
            'email': f'{self.mail}',
            'referralSource': f'{ref_code}',
            'waitlistName': 'vold',
        }

        try:
            response = session.post(
                url=url,
                headers=session.headers,
                json=json
            )

            if response.status_code == 200:
                if response.json()['waitlist']['title']:

                    return True
                else:

                    return False

        except Exception as e:
            logger.exception(f"{self.mail} | Ошибка при регистрации почты в вэйтлист: {e}")

    def check_position(self, session: tls_client.sessions.Session):
        url = "https://referlist.herokuapp.com/api/position"

        json = {
            'email': f'{self.mail}',
            'waitlistName': 'vold',
        }

        try:
            response = session.post(
                url=url,
                headers=session.headers,
                json=json,
            )

            if response.status_code == 200:
                return response.json()

        except Exception as e:
            logger.exception(f"{self.mail} | Ошибка при проверки позиции в вэйтлисте: {e}")

    def get_session(self) -> tls_client.sessions.Session:
        session = tls_client.Session(client_identifier=choice(['chrome_103',
                                                               'chrome_104',
                                                               'chrome_105',
                                                               'chrome_106',
                                                               'chrome_107',
                                                               'chrome_108',
                                                               'chrome109',
                                                               'Chrome110',
                                                               'chrome111',
                                                               'chrome112',
                                                               'firefox_102',
                                                               'firefox_104',
                                                               'firefox108',
                                                               'Firefox110',
                                                               'opera_89',
                                                               'opera_90']),
                                     random_tls_extension_order=True)
        session.headers.update(headers)

        return session
import logging

import aiohttp

from tan.settings import TOKEN_DEBUGGER


class Telegram:
    def __init__(self):
        self.TOKEN = TOKEN_DEBUGGER

        self.ADMIN_TELEGRAM = '1422194909'

        self.ID_CHAT = '1422194909'
        # self.ID_CHAT = '-1002143052926'

        self.session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)

    async def send_message(self, text):
        url_req = "https://api.telegram.org/bot" + self.TOKEN + "/sendMessage" + "?chat_id=" + \
                  self.ADMIN_TELEGRAM + "&text=" + text

        try:

            async with aiohttp.ClientSession(timeout=self.session_timeout) as session:
                async with session.get(url_req, timeout=aiohttp.ClientTimeout(total=60)) as resul:
                    response = await resul.text()

                    if resul.status != 200:
                        logging.warning(f'ошибка при отправке сообщения telegram debugger. Код "{resul.status}"')

                    return response

        except Exception as es:

            logging.warning(f'Ошибка при отправке сообщения в телеграм "{es}"')

            return False

    async def new_order(self, text):

        url_req = "https://api.telegram.org/bot" + self.TOKEN + "/sendMessage" + "?chat_id=" + \
                  self.ID_CHAT + '&parse_mode=html' + "&text=" + text

        try:

            async with aiohttp.ClientSession(timeout=self.session_timeout) as session:
                async with session.get(url_req, timeout=aiohttp.ClientTimeout(total=60)) as resul:
                    response = await resul.text()

                    if resul.status != 200:
                        logging.warning(f'ошибка при отправке заявки telegram debugger. Код "{resul.status}" "{text}"')

                    return response

        except Exception as es:

            logging.warning(f'Ошибка при отправке заявки в телеграм "{es}" "{text}"')

            return False

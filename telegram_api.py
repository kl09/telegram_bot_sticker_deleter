from utils import Request


class TelegramApi:
    API_URL = "https://api.telegram.org/bot{0}/{1}"

    def _make_request(self, token, method_name, method='get', params=None, files=None, base_url=None):
        base_url = self.API_URL if not base_url else base_url
        request_url = base_url.format(token, method_name)

        if method == 'get':
            return Request(request_url).get(params).content.get('result')

    def get_updates(self, token: str, offset: int = 0, limit: int = 100, timeout: int = 30) -> tuple:
        last_update = None

        updates = self._make_request(token=token, method_name='getUpdates', params={
            "offset": offset,
            "limit": limit,
            "timeout": timeout,
        })

        if updates and isinstance(updates, list):
            try:
                last_update = updates[-1]
            except Exception:
                last_update = updates[0]

        return updates, last_update

    def send_message(self, token: str, chat_id: int or str, text: str, parse_mode: str = None,
                     disable_web_page_preview=False, disable_notification=False, reply_to_message_id: int = None):

        parse_mode = 'Markdown' if parse_mode is None else str(parse_mode)

        return self._make_request(token=token, method_name='sendMessage', params={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": disable_web_page_preview,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id,
        })

    def delete_message(self, token: str, chat_id: int or str, message_id: str):
        return self._make_request(token=token, method_name='deleteMessage', params={
            "chat_id": chat_id,
            "message_id": message_id
        })

    def get_chat_admins(self, token: str, chat_id: int or str):
        return self._make_request(token=token, method_name='getChatAdministrators', params={
            "chat_id": chat_id,
        })

    def get_chat_info(self, token: str, chat_id: int or str):
        return self._make_request(token=token, method_name='getChat', params={
            "chat_id": chat_id,
        })

    def get_chat_member(self, token: str, chat_id: int or str, user_id: int):
        return self._make_request(token=token, method_name='getChatMember', params={
            "chat_id": chat_id,
            "user_id": user_id,
        })

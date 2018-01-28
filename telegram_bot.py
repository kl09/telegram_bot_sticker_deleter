import datetime
from telegram_api import TelegramApi


class TelegramBot:
    def __init__(self, token: str, interval_update: float = 0.1, bot_user_id: int = None):
        self.token = token
        self.api_url = "https://api.telegram.org/bot%s/" % token

        self.interval_update = interval_update
        self.bot_user_id = bot_user_id

    def start(self):
        time_worked = 0
        offset = 0

        while True:
            time = datetime.datetime.now().timestamp()
            if not time_worked or time - time_worked >= self.interval_update:
                updates, last_update = TelegramApi().get_updates(token=self.token, offset=offset)

                for update in updates:
                    message = update.get("message", None)
                    if message:
                        self._delete_sticker_from_message(message)

                if last_update:
                    offset = int(last_update.get("update_id")) + 1 if last_update else offset

                time_worked = time

    def _delete_sticker_from_message(self, message: dict):
        sticker = message.get("sticker", None)
        if sticker:
            chat_id = message.get('chat').get('id')

            result = TelegramApi().delete_message(
                token=self.token,
                chat_id=chat_id,
                message_id=message.get('message_id'),
            )

            if result is not True:
                can_delete_messages = TelegramApi().get_chat_member(
                    token=self.token,
                    chat_id=chat_id,
                    user_id=self.bot_user_id,
                ).get('can_delete_messages')

                if can_delete_messages is not True:
                    text = "Help me!! I don't have permission for deleting messages"
                else:
                    text = "Unexpected mistake :("

                TelegramApi().send_message(
                    token=self.token,
                    chat_id=chat_id,
                    text=text,
                )

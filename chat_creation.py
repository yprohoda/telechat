import asyncio

from telethon.tl.functions.messages import CreateChatRequest
from telethon.sync import TelegramClient
from asyncio import get_event_loop
from telethon import utils

from env import API_ID, API_HASH, MOBILE_NUMBER


class TelegramCompareChanel:
    def __init__(self):
        phone_number = MOBILE_NUMBER
        api_id = API_ID
        api_hash = API_HASH

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.client = TelegramClient(phone_number, api_id, api_hash, loop=self.loop)

    async def compare_chat(self, users, chat_title):
        await self.client.connect()
        user_info = await self.client.get_entity('Denys_Reckless')
        self.createdPrivateChannel = await self.client(CreateChatRequest(title=chat_title, users=users))
        self.name = utils.get_display_name(user_info)

    def get_chat_id(self):
        return self.createdPrivateChannel.__dict__["chats"][0].__dict__["id"]


def create_chat_with_users(users, chat_title, _client):
    _client.connect()
    created_chat = _client(CreateChatRequest(title=chat_title, users=users))
    created_chat_id = created_chat.__dict__["chats"][0].__dict__["id"]
    print('!!!!chat_id = ', created_chat_id)
    _conf.chat_id = created_chat_id


def get_user_info_by_name(name, _client):
    _client.connect()
    user_info = _client.get_entity(name)
    print(user_info)
    return user_info


def main():
    t_compare = TelegramCompareChanel()
    get_event_loop().run_until_complete(t_compare.compare_chat(['bananabomber'], 'test'))
    return t_compare.get_chat_id()


if __name__ == '__main__':
    pass

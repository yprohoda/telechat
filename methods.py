import asyncio

from telethon.tl.functions.messages import CreateChatRequest
from telethon.sync import TelegramClient
from asyncio import get_event_loop

from env import API_ID, API_HASH, MOBILE_NUMBER


class TelegramChanel:
    def __init__(self):
        phone_number = MOBILE_NUMBER
        api_id = API_ID
        api_hash = API_HASH

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.client = TelegramClient(phone_number, api_id, api_hash, loop=self.loop)

    async def create_private_chat(self, users, chat_title):
        await self.client.connect()
        self.created_chat = await self.client(CreateChatRequest(title=chat_title, users=users))
        await self.client.disconnect()

    def get_created_chat_id(self):
        return self.created_chat.__dict__["chats"][0].__dict__["id"]

    async def get_user_info_by_name(self, name):
        await self.client.connect()
        self.user_info = await self.client.get_entity(name)
        await self.client.disconnect()

    def get_user_id(self):
        return self.user_info.id

    async def get_user_entity_by_id(self, user_id):
        await self.client.connect()
        self.user_info = await self.client.get_entity(user_id)
        #print(self.user_info)
        await self.client.disconnect()

    def get_user_name(self):
        #print(self.user_info.username)
        return self.user_info.username


def get_user_name_func(user_id):
    telegram_chanel = TelegramChanel()
    get_event_loop().run_until_complete(telegram_chanel.get_user_entity_by_id(user_id))
    return telegram_chanel.get_user_name()


def create_chat_and_get_chat_id(user_name_list):
    telegram_chanel = TelegramChanel()
    get_event_loop().run_until_complete(telegram_chanel.create_private_chat(user_name_list, 'test'))
    return telegram_chanel.get_created_chat_id()


def get_user_id(name):
    telegram_chanel = TelegramChanel()
    get_event_loop().run_until_complete(telegram_chanel.get_user_info_by_name(name))
    return telegram_chanel.get_user_id()



# def create_chat_with_users(users, chat_title, _client):
#     _client.connect()
#     created_chat = _client(CreateChatRequest(title=chat_title, users=users))
#     created_chat_id = created_chat.__dict__["chats"][0].__dict__["id"]
#     print('!!!!chat_id = ', created_chat_id)
#
#
# def get_user_info_by_name(name, _client):
#     _client.connect()
#     user_info = _client.get_entity(name)
#     print(user_info)
#     return user_info

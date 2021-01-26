import asyncio

from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import CreateChatRequest, GetFullChatRequest
from telethon.sync import TelegramClient
from asyncio import get_event_loop

from env import API_ID, API_HASH, MOBILE_NUMBER


class TelegramChanel:
    def __init__(self):
        self.phone_number = MOBILE_NUMBER
        self.api_id = API_ID
        self.api_hash = API_HASH

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.client = TelegramClient(self.phone_number, self.api_id, self.api_hash, loop=self.loop)
        # self.client.connect()
        # if not self.client.is_user_authorized():
        #     self.client.send_code_request(self.phone_number)
        #     self.client.sign_in(self.phone_number, input('Enter code: '))


    async def create_private_chat(self, users, chat_title):
        await self.client.connect()
        if not self.client.is_user_authorized():
            await self.client.send_code_request(self.phone_number)
            await self.client.sign_in(self.phone_number, input('Enter code: '))
        self.created_chat = await self.client(CreateChatRequest(title=chat_title, users=users))
        await self.client.disconnect()

    async def get_chat_info_main(self, chat_id):
        await self.client.connect()
        self.chat_info = await self.client(GetFullChatRequest(chat_id=chat_id))
        await self.client.disconnect()

    async def get_user_info_by_name(self, name):
        await self.client.connect()
        self.user_info = await self.client.get_entity(name)
        await self.client.disconnect()

    async def get_user_entity_by_id(self, user_id):
        await self.client.connect()
        self.user_info = await self.client.get_entity(user_id)
        await self.client.disconnect()

    async def send_message(self, chat_id, message):
        await self.client.connect()
        self.s_message = await self.client.send_message(chat_id, message)
        await self.client.disconnect()

    def get_created_chat_id(self):
        return self.created_chat.__dict__["chats"][0].__dict__["id"]

    def get_user_info(self):
        return self.user_info

    def get_user_id(self):
        return self.user_info.id

    def get_user_name(self):
        return self.user_info.username

    def get_chat_info(self):
        return self.chat_info

    def message(self):
        return self.s_message


def get_user_name_func(user_id):
    telegram_chanel = TelegramChanel()
    get_event_loop().run_until_complete(telegram_chanel.get_user_entity_by_id(user_id))
    return telegram_chanel.get_user_name()


def create_chat_and_get_chat_id(user_name_list):
    telegram_chanel = TelegramChanel()
    try:
        get_event_loop().run_until_complete(telegram_chanel.create_private_chat(user_name_list, 'test'))
        return telegram_chanel.get_created_chat_id()
    except FloodWaitError as e:
        # TODO change manager-user
        return False



def get_user_id_byName(name):
    telegram_chanel = TelegramChanel()
    get_event_loop().run_until_complete(telegram_chanel.get_user_info_by_name(name))
    return telegram_chanel.get_user_id()


def get_user_info_by_UserId(user_id):
    telegram_chanel = TelegramChanel()
    get_event_loop().run_until_complete(telegram_chanel.get_user_info_by_name(user_id))
    return telegram_chanel.get_user_info()


def get_chat_info(chat_id):
    telegram_chanel = TelegramChanel()
    get_event_loop().run_until_complete(telegram_chanel.get_chat_info_main(chat_id))
    return telegram_chanel.get_chat_info()


def send_message_to_chat(chat_id, message):
    telegram_chanel = TelegramChanel()
    get_event_loop().run_until_complete(telegram_chanel.send_message(chat_id, message))
    return telegram_chanel.message()


import asyncio


from telethon.tl.functions.help import GetUserInfoRequest
from telethon.tl.functions.messages import CreateChatRequest
from telethon.sync import TelegramClient
from asyncio import get_event_loop
from telethon import functions
from asgiref.sync import async_to_sync

from env import API_ID, API_HASH, MOBILE_NUMBER

api_id = API_ID
api_hash = API_HASH
phone = MOBILE_NUMBER

# client = TelegramClient(phone, api_id, api_hash)
#
# client.connect()
# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     client.sign_in(phone, input('Enter the code: '))


def cli_connect(client):

    get_event_loop().run_until_complete(main(client))
    client.client.connect()
    return client


def create_chat_with_users(users, chat_title, _client):
    _client.connect()
    created_chat = _client(CreateChatRequest(title=chat_title, users=users))
    created_chat_id = created_chat.__dict__["chats"][0].__dict__["id"]
    return created_chat


def get_user_info_by_name(name):
    result = client(GetUserInfoRequest(user_id=name))
    print(result)

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient(phone, api_id, api_hash, loop=loop)
    get_event_loop().run_until_complete(create_chat_with_users(users=['bananabomber'], chat_title='asdf', _client=client))

    loop.close()


if __name__ == '__main__':
    pass
    # create_chat_with_users(users=['bananabomber', 'Listing_on_P2PB2B'], chat_title='asdf')
    create_chat_with_users(users=['bananabomber'], chat_title='asdf')

    get_user_info_by_name('alexspark21')

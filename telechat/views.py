from datetime import datetime
from django.http import HttpResponse
from telethon.tl.functions.messages import CreateChatRequest
from methods import create_chat_and_get_chat_id_main, get_user_id_main
from telechat.models import Chat
from telethon.sync import TelegramClient
from env import API_ID, API_HASH, MOBILE_NUMBER

api_id = API_ID
api_hash = API_HASH
phone = MOBILE_NUMBER
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))


def index(request):

    name = 'bananabomber'

    # get id of user in telegram
    user_id = str(get_user_id_main(name))

    # display info on the web page
    info = check_existing_chat_for_user_id(user_id) + ' for User_id=' + user_id
    return HttpResponse(info)

def check_existing_chat_for_user_id(user_id):

    '''
    Check existing chat in db
    :return: chat_id
    '''

    chat_info = check_records_with_name(user_id)
    print(chat_info)
    if chat_info:
        chat_info = [i for i in chat_info]
        print('chat_info', *chat_info)
        chat_id = 'Existing chat is found=' + str(chat_info[0])
    else:
        chat_id = 'New chat is created=' + str(create_chat_and_get_chat_id_main())
    return chat_id

def create_record_db(user_id, chat_id, manager_id):
    record = Chat(
        user_id=user_id,
        chat_id=chat_id,
        manager_id=manager_id,
        date=datetime.now()
    )
    record.save()
    return f"Record {record} is saved"


def get_all_records():
    # return Chat.objects.all()  # same: Chat.objects.filter()
    return Chat.objects.filter()


def check_records_with_name(user_id):
    result = Chat.objects.filter(user_id=user_id)
    if result:
        return result
    else:
        return False


def create_chat_with_users(users, chat_title):
    createdPrivateChannel = client(CreateChatRequest(title=chat_title, users=users))
    newChannelID = createdPrivateChannel.__dict__["chats"][0].__dict__["id"]
    return newChannelID


def get_user_info_by_name(name):
    info = client.get_entity(name)
    print(info)
    return info

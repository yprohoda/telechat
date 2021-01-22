from datetime import datetime
from django.http import HttpResponse
from telethon.tl.functions.messages import CreateChatRequest
from chat_creation import main
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

    chat_id = str(main())

    return HttpResponse(chat_id)


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


def get_records_with_name(name):
    result = Chat.objects.filter(user_id=name)
    if result:
        return result
    else:
        raise Exception(f"No record {name} is found")


def create_chat_with_users(users, chat_title):
    createdPrivateChannel = client(CreateChatRequest(title=chat_title, users=users))
    newChannelID = createdPrivateChannel.__dict__["chats"][0].__dict__["id"]
    return newChannelID


def get_user_info_by_name(name):
    info = client.get_entity(name)
    print(info)
    return info

import asyncio
import webbrowser
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from telethon import TelegramClient

from env import MOBILE_NUMBER, API_ID, API_HASH
from methods import create_chat_and_get_chat_id, get_user_id_byName, send_message_to_chat, get_user_info_by_UserId
from telechat.models import Chat

NAME = 'bananabomber'  # id = 160718418
OLD_CHAT = 'https://t.me/Listing_on_P2PB2B'
MESSAGE = f'Hello, {NAME}, Welcome to P2PB2B'
LINK_TO_CHAT = 'https://web.telegram.org/#/im?p=c'
MANAGER_ID = '1'


# TODO check number of created chats
# TODO-Front create captcha on request

def test_form(request):
    """ http://127.0.0.1:8000/telechat/form """
    if request.method == "POST":
        # user = request.POST.get('username')
        # if user == "mark":
        #     return HttpResponse('hello mark')
        get_text = request.POST.get("username")

        def auth(code):
            phone_number = MOBILE_NUMBER
            api_id = API_ID
            api_hash = API_HASH

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(phone_number, api_id, api_hash, loop=loop)
            client.connect()
            if not client.is_user_authorized():
                client.send_code_request(phone_number)
                client.sign_in(phone_number, code)

        auth(get_text)

    return render(request, "form.html")


def index(request):
    name = NAME

    info = get_user_info_by_UserId(1542151274)
    print(info)

    # check user id in telegram
    user_id = check_user_name_is_valid(name)
    print('User_id =', user_id)

    if user_id:
        existing_chat = check_existing_chat_for_user_id(int(user_id))
        if not existing_chat:
            chat_id = create_chat_and_get_chat_id([name])
            if chat_id:
                create_record_db(user_id, chat_id, MANAGER_ID)
                info = 'New chat is created'
                send_message_to_chat(chat_id=chat_id, message=MESSAGE)
                webbrowser.open(LINK_TO_CHAT + f'{chat_id}', new=2)  # redirect to new-created chat
            else:
                info = 'Error happened'
        else:
            info = f'Existing chat is found={existing_chat}'
            webbrowser.open(LINK_TO_CHAT + f'{str(existing_chat)}', new=2)  # redirect to existing chat
    else:
        # Redicted to old style
        info = f'User "{name}" is not found'
        webbrowser.open(OLD_CHAT, new=2)

    return HttpResponse(info)


def check_user_name_is_valid(user_name):
    """
    Checks if user is valid and have user_id
    :param user_name:
    :return: True or False
    """
    try:
        user_id = str(get_user_id_byName(user_name))
        print(f'User {user_name} is valid')
        return user_id
    except Exception as e:
        return False


def check_existing_chat_for_user_id(user_id):
    """
    Checks existing chat in db.
    Creates chat if it doesn't exist.
    :return: chat_id
    """

    chat_info = check_records_with_name(user_id)
    if chat_info:
        for i in chat_info:
            chat_id = i

        return chat_id  # 'Existing chat is found'
    else:
        return False  # 'Existing chat is NOT found'


def create_record_db(user_id, chat_id, manager_id):
    record = Chat(
        user_id=str(user_id),
        chat_id=str(chat_id),
        manager_id=str(manager_id),
        date=datetime.now()
    )
    record.save()
    return f"Record {record} is saved"


def check_records_with_name(user_id):
    result = Chat.objects.filter(user_id=user_id)
    if result:
        return result
    else:
        return False

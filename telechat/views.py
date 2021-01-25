from datetime import datetime
from django.http import HttpResponse
from methods import create_chat_and_get_chat_id, get_user_id, get_user_name_func
from telechat.models import Chat

NAME = 'bananabomber'  # id = 160718418
MANAGER_ID = '1'

def index(request):
    name = NAME

    # check user id in telegram
    user_id = check_user_name_is_valid(name)
    print('User_id =', user_id)

    #
    if user_id:
        if not check_existing_chat_for_user_id(int(user_id)):
            chat_id = create_chat_and_get_chat_id([name])
            create_record_db(user_id, chat_id, MANAGER_ID)
            info = 'New chat is created'
        else:
            info = 'Existing chat is found'
            # TODO redirect to existing chat - http://127.0.0.1:8000/telechat/
    else:
        info = f'User "{name}" is not found'
        # TODO redicted to old style chat - https://t.me/Listing_on_P2PB2B

    return HttpResponse(info)


def check_user_name_is_valid(user_name):
    """
    Checks if user is valid and have user_id
    :param user_name:
    :return: True or False
    """
    try:
        user_id = str(get_user_id(user_name))
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
        return True  # 'Existing chat is found'
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

# def get_all_records():
#     # return Chat.objects.all()  # same: Chat.objects.filter()
#     return Chat.objects.filter()

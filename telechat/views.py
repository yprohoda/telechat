from datetime import datetime
from django.http import HttpResponse
from methods import create_chat_and_get_chat_id, get_user_id, get_user_name_func
from telechat.models import Chat

NAME = 'bananabomber'  # id = 160718418


# TODO check incorrect name - if name is incorrect make old redirect
# TODO if name is correct, then:
# TODO make redirect to new chat / old chat
# TODO create_chat_and_get_chat_id_main (__name__)

def index(request):
    name = NAME

    # check user id in telegram
    user_id = check_user_name_is_valid(name)
    print('User_id =', user_id)

    #
    if user_id:
        if not check_existing_chat_for_user_id(int(user_id)):
            info = create_chat_and_get_chat_id([name])
        else:
            info = 'Existing chat is found'
    else:
        info = f'User "{name}" is not found'

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

    user_name = get_user_name_func(user_id)
    print('!!!!!!', user_name)

    chat_info = check_records_with_name(user_id)
    print(chat_info)
    if chat_info:
        chat_info = [i for i in chat_info]
        print('chat_info', *chat_info)
        info = 'Existing chat is found=' + str(chat_info[0])
        print(info)
        return True
    else:
        print('Existing chat is NOT found')
        return False


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

import asyncio
from datetime import datetime
from django.http import HttpResponse
from chat_creation import main, create_chat_with_users
from telechat.models import Chat


def index(request):
    #result = create_record_db(1, 'Bob', 3, 2)
    print(get_records_with_user_nick('Bob'))
    # all_records = get_all_records()
    # return HttpResponse(f"I'm telechat bot! Result: {result}. All records: {all_records}")
    # return HttpResponse(f"I'm telechat bot! All records: {str(all_records)}")

    # main()
    queryset = Chat.objects.all()
    print('Chat ids:', [i.chat_id for i in queryset])
    print('User ids:', [i.user_id for i in queryset])

    create_chat_with_users(users=['bananabomber'], chat_title='asdf')

    return HttpResponse(f"I'm telechat bot!")


# def create_chat_with_users(users, chat_title):
#     createdPrivateChannel = client(CreateChatRequest(title=chat_title, users=users))
#     newChannelID = createdPrivateChannel.__dict__["chats"][0].__dict__["id"]
#     return newChannelID


def create_record_db(user_id, user_nick, chat_id, manager_id):
    record = Chat(
        user_id=user_id,
        user_nick=user_nick,
        chat_id=chat_id,
        manager_id=manager_id,
        date=datetime.now()
    )
    record.save()
    return f"Record {record} is saved"


def get_all_records():
    # return Chat.objects.all()  # same: Chat.objects.filter()
    return Chat.objects.filter()


def get_records_with_user_id(user_id):
    result = Chat.objects.filter(user_id=user_id)
    if result:
        print(f'Record {user_id} is found')
        return result
    else:
        raise Exception(f"No records {user_id} is found")


def get_records_with_user_nick(user_nick):
    result = Chat.objects.filter(user_nick=user_nick)
    if result:
        print(f'Record {user_nick} is found')
        return result
    else:
        raise Exception(f"No records {user_nick} is found")

def get_chat_id_by_user_nick(user_nick):
    result = Chat.objects.filter(user_nick=user_nick)
    print(result)



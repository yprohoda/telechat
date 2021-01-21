from datetime import datetime
from django.http import HttpResponse
from chat_creation import main
from telechat.models import Chat


def index(request):
    # result = create_record_db(1, 3, 2)
    # all_records = get_all_records()
    # return HttpResponse(f"I'm telechat bot! Result: {result}. All records: {all_records}")
    #
    #
    # return HttpResponse(f"I'm telechat bot! All records: {str(all_records)}")

    main()
    #print(get_all_records())
    #print(get_records_with_name("111"))
    return HttpResponse(f"I'm telechat bot! {get_all_records()}")


# def create_chat_with_users(users, chat_title):
#     createdPrivateChannel = client(CreateChatRequest(title=chat_title, users=users))
#     newChannelID = createdPrivateChannel.__dict__["chats"][0].__dict__["id"]
#     return newChannelID


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
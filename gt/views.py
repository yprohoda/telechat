import json
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from geetest import GeetestLib

# captcha_id = "b46d1900d0a894591916ea94ea91bd2c"
# private_key = "36fc3fe98530eea08dfc6ce76e3d24c4"
captcha_id = "05592804de5811e179d9964f356d6149"
private_key = "d1f495d8128425b92c40d74ce0e7361d"


OLD_CHAT = 'https://t.me/Listing_on_P2PB2B'
TEST_CHAT = 514018926
LINK_TO_CHAT = 'https://web.telegram.org/#/im?p=c'



def home(request):
    return render(request, template_name="index.html")


def getcaptcha(request):
    # user_id = 'test'
    user_id = random.randint(1, 100)

    gt = GeetestLib(captcha_id, private_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


def validate(request):
    if request.method == "POST":
        gt = GeetestLib(captcha_id, private_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            return true
        else:
            return false

    return false


from django.shortcuts import render
from django.http import HttpResponse
from pyfcm import FCMNotification
# Create your views here.
from django.shortcuts import render
from .forms import InputForm


# Create your views here.
def home_view(request):
    push_service = FCMNotification(api_key="AAAA-VpvPgs:APA91bFN6tcNosEz81mDxZEgwjb3KkL-_Oc_dxU_u9SDmGDWNGRozy-7-B_rKD59rURmeaLMRA0C8hn5gUtV3puCkCwHWMuNlBf31Dk9BJVokG-qlHbA2PfYAVVAsgNNky7JSRIgrL4b")
    context = {}
    context['form'] = InputForm()
    if 'sub' in request.POST:
        token=request.POST.get('registration_token')
        title=request.POST.get('title')
        message=request.POST.get('message')
        #token,title,message = request.POST['registration_token', 'title', 'body']
        result = push_service.notify_single_device(registration_id=token,message_title=title, message_body=message)
        print(result)
        print(token,title)
    return render(request, "home.html", context)

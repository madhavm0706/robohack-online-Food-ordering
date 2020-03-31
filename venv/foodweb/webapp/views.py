from django.shortcuts import render
from webpush import send_user_notification

payload = {"head": "Welcome!", "body": "Hello World"}

#ye wala part jb lgaio jb notification bhejna ho
send_user_notification(user=user, payload=payload, ttl=1000)
# Create your views here.
def index(request):
    return render(request,'webapp/index.html',{})
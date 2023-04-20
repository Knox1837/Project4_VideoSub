from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from datetime import date
import random
class Sub_body(View):
    def get(self, request):
        return render(request, "user/register.html")
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        return render(request, "user/register.html")

class Subscribe(View):
    def get(self, request):
        return render(request, 'user/subscribe.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password = password)
        time = str(date.today())
        youtube_links = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "https://www.youtube.com/watch?v=Iwuy4hHO3YQ",
        "https://www.youtube.com/watch?v=z5rRZdiu1UE",
        "https://www.youtube.com/watch?v=3tmd-ClpJxA",
        "https://www.youtube.com/watch?v=NHozn0YXAeE",
        "https://www.youtube.com/watch?v=8CdcCD5V-d8",
        "https://www.youtube.com/watch?v=iLBBRuVDOo4",
        "https://www.youtube.com/watch?v=G7IwOgpSbU4",
        "https://www.youtube.com/watch?v=EE-xtCF3T94",
        "https://www.youtube.com/watch?v=XbGs_qK2PQA",
        "https://www.youtube.com/watch?v=0nRvjsTIfU8",
        "https://www.youtube.com/watch?v=d0qDWdWldfM",
        "https://www.youtube.com/watch?v=kffacxfA7G4",
        "https://www.youtube.com/watch?v=YykjpeuMNEk",
        "https://www.youtube.com/watch?v=JwYX52BP2Sk",
        "https://www.youtube.com/watch?v=9HDEHj2yzew",
        "https://www.youtube.com/watch?v=UceaB4D0jpo",
        "https://www.youtube.com/watch?v=IcrbM1l_BoI",
        "https://www.youtube.com/watch?v=QGJuMBdaqIw"
        ]
        rand = random.randint(1,19)
        if user:
            login(request, user)
            send_mail(
                "Daily video", # subject
                time +":\n Daily Video Subscription:\n"+ youtube_links[rand], # body
                'xentime6@gmail.com', # sender
                [user.email] # receiver(CC:)
            )
            return render(request, 'user/subscribe.html', {"message": "Successfully subscribed"})
        return render(request, 'user/subscribe.html')
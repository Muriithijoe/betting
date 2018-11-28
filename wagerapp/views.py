from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Bets, UserProfile
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request):
    bets = Bets.get_all()
    return render(request,'index.html',{'bets':bets})

@login_required(login_url='/accounts/login/')
def categories(request):
    return render(request,'make_wager.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile =UserProfile.objects.filter(username=current_user)

    if len(profile)<1:
        profile = "No profile"
    else:
        profile = UserProfile.objects.filter(username=current_user)

    return render(request, 'profile.html',{'profile':profile})

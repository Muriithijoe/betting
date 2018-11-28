from django.shortcuts import render

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')

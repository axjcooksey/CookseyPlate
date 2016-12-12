from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.utils.html import escape
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.template import loader
import simplejson as json
from .forms import *
from django.contrib.auth import authenticate, login
from models import Fixture, Selection

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    round_list = Fixture.objects.order_by('round_no')[:23]
    template = loader.get_template('home.html')
    context = {
        'round_list': round_list,
    }
    return HttpResponse(template.render(context, request))

#def index(request):
#    game_list = Fixture.objects.order_by('game_no')[:18]
#    template = loader.get_template('home.html')
#    context = {
#        'game_list': game_list,
#    }
#    return HttpResponse(template.render(context, request))

#def detail(request, round_no):
#    return HttpResponse("You're looking at round %s." % round_no)

def detail(request, round_no):
    try:
        game_list = Fixture.objects.filter(round_no=1).order_by('game_no')
    except Fixture.DoesNotExist:
        raise Http404("Round does not exist")
    return render(request, 'detail.html', {'game_list': game_list})

#def detail(request, game_no):
#    try:
#        game = Fixture.objects.get(pk=game_no)
#    except Fixture.DoesNotExist:
#        raise Http404("Game does not exist")
#    return render(request, 'polls/detail.html', {'question': question})

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            print(login(request, user))
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request,'register.html', {'form':form})

# Previously somewhat functioning view
#    round1 = Fixture.objects.order_by('game_no')[:7]
#    home_team = Fixture.home_team
#    template = loader.get_template('plate/templates/home.html')
#    context = {
#        'round1': round1,
#        'home_team': home_team

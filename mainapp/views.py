from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,UserPassesTestMixin
from .models import Community,MarketPost, Leader, Community_Event
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import Feedback
from .forms import FeedbackForm





def home(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()

    patrons = Leader.objects.filter(category='Patron')
    events = Community_Event.objects.all()
    chairpersons = Leader.objects.filter(category='Chairperson')
    vicechairpersons = Leader.objects.filter(category='Vice-Chairperson')
    secretarys = Leader.objects.filter(category='Secretary')

    context = {
        'form':form,
        'patrons':patrons,
        'events':events,
        'chairpersons':chairpersons,
        'vicechairpersons':vicechairpersons,
        'secretarys':secretarys,
    }

    return render(request,'home.html',context)


def contact(request):
    return render(request,'contact.html')

class CommunityListView(ListView):
    model = Community
    template_name = "Comunity/listcomunity.html"
    paginate_by = 8

class CommunityDetailView(DetailView):
    model = Community
    template_name = "Comunity/detailcommunity.html"

def comsearch(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Community.objects.all().filter(name=search)
        return render(request,'Comunity/comsearch.html',{'post':post})

class LeadersListView(ListView):
    model = Leader
    template_name = 'leader/leader_list.html'
    context_object_name = 'leaders'

class LeaderDetailView(DetailView):
    model = Leader
    template_name = 'leader/leader_detail.html'

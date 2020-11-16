from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Community
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html') 

def about(request):
    return render(request,'about.html')  

class CommunityListView(ListView): 
    model = Community
    template_name = "Comunity/listcomunity.html"
    paginate_by = 8


def comsearch(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Community.objects.all().filter(name=search)
        return render(request,'comsearch.html',{'post':post})

class CommunityDetailView(DetailView):
    model = Community
    template_name = "Comunity/detailcommunity.html"
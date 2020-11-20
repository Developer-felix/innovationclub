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
    }

    return render(request,'home.html',context)

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
        return render(request,'Comunity/comsearch.html',{'post':post})

class CommunityDetailView(DetailView):
    model = Community
    template_name = "Comunity/detailcommunity.html"


# class CommunityDeleteView(DeleteView):
#     model = Community
#     template_

# market place home page list views
def market_home(request):
    posts = MarketPost.objects.all()
    context ={
        'posts':posts,
        'title':'blog_home',
    }
    return render(request,'market/home.html',context)

def market_detail(request, pk):
    posts = MarketPost.objects.get(pk=pk)
    context = {
        'posts':posts
    }
    return render(request,'market/market_detail.html',context)

class MarketCreateView(LoginRequiredMixin, CreateView):
    model = MarketPost
    template_name = 'market/market_form.html'
    fields = ['type_of_item','description','contact','image','location','quantity']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)   
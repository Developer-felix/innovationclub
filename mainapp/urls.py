from django.urls import path 
from .views import( 
                    MarketCreateView,
                   
                   
                  )   
from . import views


urlpatterns = [
 path("", views.home, name="home-page"), 
 path("about/", views.about, name="about-page"), 
 path("contact_Us", views.contact, name="contact-page"),
 path("Search/", views.comsearch, name="cmsearch"),  
 path('communities/',views.CommunityListView.as_view(), name='community-list'),
 path('community/<slug>/',views.CommunityDetailView.as_view(),name="comunity-detail"),
   #market urls
     path('market/',views.market_home,name='market-home'),#working list view
     path('market/<int:pk>/',views.market_detail,name='market_detail'),#working detail view
     path('market/post/new/',MarketCreateView.as_view(), name='market-create'),#working create view
]


from django.urls import path 
from . import views

urlpatterns = [
 path("", views.home, name="home-page"), 
 path("contact_Us", views.contact, name="contact-page"), 
 path('communities/',views.CommunityListView.as_view(), name='community-list'),
 path('community/<slug>/',views.CommunityDetailView.as_view(),name="comunity-detail"),
]


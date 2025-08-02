from django.urls import path
from . import views

app_name = 'daily_tracker'

urlpatterns = [
    path('tracker/', views.tracker_view, name='tracker'),
    path('record/', views.record_daily_view, name='record_daily'),
    path('search-users/', views.search_users, name='search_users'),
] 
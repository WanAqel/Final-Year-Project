from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('',views.events_home, name='home'),
    # path('new-event/',views.event_new, name='new-event'),
    path('<slug:slug>', views.event_page, name='page'),
]
from django.contrib import admin
from django.contrib.admin.widgets import AdminSplitDateTime
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'start_datetime': AdminSplitDateTime(),  
            'end_datetime': AdminSplitDateTime(),
        }

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = ('name', 'start_datetime', 'end_datetime', 'status', 'category', 'fees')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'category')
    list_filter = ('status', 'category')

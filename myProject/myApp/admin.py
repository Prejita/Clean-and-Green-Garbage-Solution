from django.contrib import admin
from .models import DustbinData,Notification,Event

admin.site.register(DustbinData)
admin.site.register(Notification)
admin.site.register(Event)
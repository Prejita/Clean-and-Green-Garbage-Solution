from django.contrib import admin
from .models import DustbinData,Notification,Event,Registration

admin.site.register(DustbinData)
admin.site.register(Notification)
admin.site.register(Event)
admin.site.register(Registration)
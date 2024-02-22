from django.contrib import admin
from .models import DustbinData,Notification,Event,Registration,AcceptedRegistration,DeclinedRegistration

admin.site.register(DustbinData)
admin.site.register(Notification)
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(AcceptedRegistration)
admin.site.register(DeclinedRegistration)
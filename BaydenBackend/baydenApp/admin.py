from django.contrib import admin
from .models import Events, Attendee, Subscriber

# Register your models here.
class Eventadmin(admin.ModelAdmin):
    Model = Events
    list_display = ("name",)

class Attendeeadmin(admin.ModelAdmin):
    model = Attendee
    list_display = ("firstname", "email")

class Subscriberadmin(admin.ModelAdmin):
    model = Subscriber
    list_display = ("firstname", "email", "lastname")

admin.site.register(Subscriber, Subscriberadmin)
admin.site.register(Events, Eventadmin)
admin.site.register(Attendee, Attendeeadmin)

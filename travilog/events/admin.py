from django.contrib import admin
from events.models import Event, Person


class PersonInline(admin.TabularInline):
	model = Person


class EventAdmin(admin.ModelAdmin):
    inlines = [PersonInline]
    list_display = ['title', 'date', 'location']

admin.site.register(Event, EventAdmin)
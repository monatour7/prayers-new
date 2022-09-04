from django.contrib import admin

from prayers.prayersapp.models import PrayersTime

@admin.register(PrayersTime)
class PersonAdmin(admin.ModelAdmin):
    pass
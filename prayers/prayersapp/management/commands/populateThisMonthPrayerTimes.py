import requests
from django.core.management.base import BaseCommand
from django.shortcuts import redirect

from prayers.prayersapp.models import PrayersTime

class Command(BaseCommand):
    help = 'HI is displayed'

    def handle(self, *args, **kwargs):
        response = requests.get('https://api.aladhan.com/v1/calendar?latitude=32.185839&longitude=34.981255&month=8&year=2022')
        data = response.json()["data"]
        for i in range(len(data)):
            pt = PrayersTime(date=data[i]['date']['readable'], prayerTimes=data[i]['timings'])
            pt.save()

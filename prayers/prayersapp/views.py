from django.http import JsonResponse
from prayers.prayersapp.models import PrayersTime


def index(request):
    result = PrayersTime.objects.all()

    newRes = result[29].prayerTimes
    newRes['fajr'] = newRes['Fajr']
    del newRes['Fajr']
    newRes['sunrise'] = newRes['Sunrise']
    del newRes['Sunrise']
    newRes['duhur'] = newRes['Dhuhr']
    del newRes['Dhuhr']
    newRes['asr'] = newRes['Asr']
    del newRes['Asr']
    newRes['sunset'] = newRes['Sunset']
    del newRes['Sunset']
    newRes['maghrib'] = newRes['Maghrib']
    del newRes['Maghrib']
    newRes['isha'] = newRes['Isha']
    del newRes['Isha']
    newRes['imsak'] = newRes['Imsak']
    del newRes['Imsak']
    newRes['midnight'] = newRes['Midnight']
    del newRes['Midnight']
    newRes['first-third'] = newRes['Firstthird']
    del newRes['Firstthird']
    newRes['last-third'] = newRes['Lastthird']
    del newRes['Lastthird']
    return JsonResponse(newRes)

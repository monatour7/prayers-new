from rest_framework import serializers
from prayers.prayersapp.models import PrayersTime


class PrayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayersTime
        fields = ('date', 'prayerTimes')

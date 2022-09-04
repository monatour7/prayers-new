from django.db import models
import jsonfield


class PrayersTime(models.Model):
    date = models.CharField(max_length=20, null=True)
    prayerTimes = jsonfield.JSONField(null=True)
    objects = models.Manager

    def __str__(self):
        return self.prayerTimes
    class Meta:
        verbose_name = ("PrayersTime")
        verbose_name_plural = ("PrayersTime")
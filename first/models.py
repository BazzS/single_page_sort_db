from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime
# Create your models here.

class Mat(models.Model):
    match_date = models.DateField(default=timezone.localdate,verbose_name="Дата", blank=False)
    match_name = models.CharField(max_length=100, verbose_name="Название", blank=False,)
    match_count = models.SmallIntegerField(default=100, verbose_name="Количество зрителей",blank=False)
    match_distance = models.FloatField(verbose_name="Расстояние",blank=False)

    def __str__(self):
        return self.match_name

    def save(self,*args,**kwargs):
        if self.match_count < 0 or self.match_count > 10000:
            raise ValidationError ("Count can't be less 0 and more than 10000")
        if self.match_date < datetime.date.today():
            raise ValidationError("Day of match can't be smaller that today's date")
        if self.match_distance < 0:
            raise ValidationError("Distance may be positive")

        super(Mat,self).save(*args,**kwargs)

    class Meta:
        verbose_name = "Матч"
        verbose_name_plural = "Maтчи"
        ordering = ['match_date']

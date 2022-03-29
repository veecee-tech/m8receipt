from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime
# Create your models here.

class Receipt(models.Model):
    receipt_no = models.CharField(max_length=50, null=True, blank=True)
    received_from = models.CharField(max_length=255, blank=False, null=False)
    amount_in_words = models.CharField(max_length=500, blank=False, null=False)
    payment_for = models.CharField(max_length=255, blank=False, null=False)
    amount_in_figure = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.receipt_no} - {self.received_from}"

@receiver(post_save, sender=Receipt)
def create_receipt(sender, instance, created, **kwargs):
    r = Receipt.objects.get(id = instance.id)
    if created:
        yr = int(datetime.date.today().strftime('%Y'))
        dt = int(datetime.date.today().strftime('%d'))
        mt = int(datetime.date.today().strftime('%m'))
        d = datetime.date(yr,mt,dt)
        current_date = d.strftime("%Y%m%d")
        if instance.id < 10:
            pad_no = "00"
        elif instance.id >=10 and instance.id < 100:
            pad_no = "0"
        else: 
            pad_no = ""
        receipt_no = current_date + pad_no + str(instance.id)
        r.receipt_no = receipt_no

        r.save()
    else:
        pass


    
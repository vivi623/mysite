from django.db import models

# Create your models here.
class Ordernums(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouseno = models.CharField(max_length=20)
    ordernum = models.IntegerField()
    orderdate = models.DateField()

    class Meta:
        app_label = 'showinfo'
        db_table = 'ordernums'


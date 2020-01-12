from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):

    class Meta:
        db_table="category"

    category_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.category_name

class Kakeibo(models.Model):

    class Meta:
        db_table="kakeibo"

    date = models.DateField(verbose_name="Date", default=datetime.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    money = models.IntegerField(verbose_name="Amount", help_text="Aus Dollar")
    memo = models.CharField(verbose_name="Memo", max_length=500)

    def __str__(self):
        return self.memo

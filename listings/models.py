from django.db import models
from realtors.models import Realtor
from listings.choices import district_choices               #field可以選擇
# Create your models here.

class Listing(models.Model):
    list_date = models.DateField(auto_now_add=True)                             #記得當時创建日期，會用黎做排序，不會顯示data 
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)       # realtor出name因為realtor model's self name   + listing副指去主;  if del listing , 不影響del realtor 
    title = models.CharField(max_length=200)                    #短文本
    price = models.IntegerField()                               
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=50, choices=district_choices.items())        #field可以選擇
    description = models.TextField(blank=True)                  #長文本
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    clubhouse = models.IntegerField()
    sqrt = models.IntegerField()
    estate_size = models.FloatField(default=0.0)
    is_published = models.BooleanField(default=True)
    phtoto_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        ordering = ('-list_date',)                          #database用list_date黎排, 要黎web行快d
        indexes = [models.Index(fields=['list_date'])]          #为 list_date 创建索引

    def __str__(self):
        return self.title
    



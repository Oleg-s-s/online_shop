from distutils.command.upload import upload
from django.db import models

class Goods(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to="files/", null=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'
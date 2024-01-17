from django.db import models

# from django.core.files.storage import FileSystemStorage
class Data(models.Model):
  ids=models.AutoField(primary_key=True)
  name=models.CharField(max_length=100)
  mob=models.IntegerField()
  email=models.EmailField()
  password=models.CharField(max_length=100)
  
  image = models.ImageField(upload_to='images/',null=True,blank=True)
  # duration = models.DurationField()
  # filee=models.FileField(upload_to='uploads/',storage=custom_storage)


# Create your models here.

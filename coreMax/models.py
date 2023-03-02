from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    image=models.ImageField(upload_to='projects/')
    url=models.URLField(blank=True) 

class Hobbies(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    image=models.ImageField(upload_to='cv/')
    url=models.URLField(blank=True) 

class Work(models.Model):
        title=models.CharField(max_length=100)
        Institution=models.CharField(max_length=50)
        Work_description=models.TextField(max_length=250)
        start_date=models.DateField()
        end_date=models.DateField(blank=True, null=True)

level=(
     ('primary','primary'),
     ('secondary','secondary'),
      ('Technical Course', 'Technical Course'),
     ('Undergraduate', 'Undergraduate'),
     ('Masters', 'Masters'),
      ('PhD', 'PhD'),
)      

class Education(models.Model):
    certification=models.CharField(max_length=100, choices=level)
    school=models.CharField(max_length=50)
    start_date=models.DateField()
    end_date=models.DateField(blank=True, null=True)

class Skills(models.Model):
     language=models.CharField(max_length=50)
     level=models.PositiveIntegerField()

class Contact(models.Model):
     birth_date=models.DateField()
     name=models.CharField(max_length=20)
     phone=models.CharField(max_length=15)
     email=models.CharField(max_length=50)
     weblink=models.CharField(blank=True, null=True, max_length=150)

class IndexBody(models.Model):
     icon=models.ImageField(upload_to='projects/')
     ContentName=models.CharField(max_length=10)
     ContentDesc=models.CharField(max_length=250)
     







    
















      

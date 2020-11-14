from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Leader(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    contact = models.IntegerField()
    role = models.TextField(max_length=500)
    image = models.ImageField(upload_to='leader_images/')
    
    def __str__(self):
        return f'{self.name} - {self.course}'

class  Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact =models.CharField(max_length=20)
    leader = models.ForeignKey(Leader,on_delete=models.CASCADE)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='comunity_images/')
    def __str__(self):
        return f'{self.name} Lead By {self.leader}'

    def get_absolute_url(self):
        return reverse("comunity-detail",kwargs={
            'slug' : self.slug
        })    

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    community = models.ForeignKey(Community,on_delete=models.CASCADE)
    source_code = models.URLField(max_length=1000)
    live_demo = models.URLField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f'{self.title} Lead By {self.community}'


    

    
    
    

    
    
    
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

#imagekit
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Feedback(models.Model): 
  
    # fields of the model 
    name = models.CharField(max_length = 200) 
    message = models.TextField() 
  
    # renames the instances of the model 
    # with their title name 
    def __str__(self): 
        return f'{self.name } - {self.message}'

LEADERS_CATEGORY = (
    ('Patron','Patron'),
    ('Chairperson','Chairperson'),
    ('Vice-Chairperson','Vice-Charperson'),
    ('Secretary', 'Secretary'),
    ('Organizing Sec', 'Organizing Sec'),
    ('Treasurer','Treasurer'),
    ('Auditor','Auditor'),
    ('AI $ IoT team Lead','AI $ IoT team Lead'),
    ('Cyber Security Lead','Cyber Security Lead'),
    ('Opensource Comm Lead','Opensource Comm Lead'),
    ('Future comm lead','Future comm lead'),
)

class Leader(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    contact = models.IntegerField()
    category = models.CharField(choices=LEADERS_CATEGORY, max_length=100, blank=True)
    role = models.TextField(max_length=500)
    image = models.ImageField(upload_to='leader_images/')
    image_thumbnail = ImageSpecField(source = 'image',
                                    processors=[ResizeToFill(150,150)],
                                    format='JPEG',
                                    options={'quality':100})
    
    def __str__(self):
        return f'{self.name} - {self.category}'

class  Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact =models.CharField(max_length=20)
    leader = models.ForeignKey(Leader,on_delete=models.CASCADE)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='comunity_images/')
    #image_thumbnail = ResizeToFit(source='image',
                               # processor=[ResizeToFit(500,500)])

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

class MarketPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_item = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    description =models.TextField(max_length=500,default="About my sales")
    image = models.FileField(upload_to="marketplace/")
    contact = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.type_of_item}-{self.quantity}"
    def get_absolute_url(self):
        return reverse('market_detail', kwargs={'pk':self.pk})


class Community_Event(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    venue = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    image = models.ImageField(upload_to='event_images')
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(1024,768)],
                                    format='JPEG',
                                    options = {'quality':70})
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField()

    def __str__(self):
        return f'{self.title} by {self.community}'

    
    
    

    
    
    
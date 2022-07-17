from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from datetime import datetime
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class City(models.Model):
    cityid =models.AutoField(primary_key=True)
    name = models.CharField( max_length=50)

    class Meta:
        verbose_name = ("City")
        verbose_name_plural = ("Cities")

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    ab = instance.date.strftime("%Y/%m/%d")
    return 'pdf/{0}/{1}/{2}'.format(instance.city.name,ab, filename)


class DailyFeed(models.Model):
    abc =  datetime.today().strftime("%Y/%m/%d")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    page1 = CloudinaryField('page1',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page2 = CloudinaryField('page2',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page3 = CloudinaryField('page3',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page4 = CloudinaryField('page4',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page5 = CloudinaryField('page5',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page6 = CloudinaryField('page6',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page7 = CloudinaryField('page7',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page8 = CloudinaryField('page8',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page9 = CloudinaryField('page9',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page10 = CloudinaryField('page10',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page11 = CloudinaryField('page11',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])
    page12 = CloudinaryField('page12',folder = '{}'.format(abc) ,transformation=[{"quality":"auto:best",}])

class TestDailyFeed(models.Model):
    abc =  datetime.today().strftime("%Y/%m/%d")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    page1 = models.FileField(upload_to=user_directory_path)

def special_directory_path():
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    yesterday = datetime.now()
    ab = datetime.now().date.strftime("%Y/%m/%d")
    return '{}'.format(ab)

class DailySpecialAkola(models.Model):
    id = models.AutoField(primary_key=True)
    date =models.DateField(auto_now=False, auto_now_add=False)
    specialakola1  = CloudinaryField('specialakola1',transformation=[{"quality":"auto:best",}])
    specialakola2 = CloudinaryField('specialakola2',transformation=[{"quality":"auto:best",}])
    specialakola3 = CloudinaryField('specialakola3',transformation=[{"quality":"auto:best",}])
    specialakola4 = CloudinaryField('specialakola4',transformation=[{"quality":"auto:best",}])
    specialakola5 = CloudinaryField('specialakola5',transformation=[{"quality":"auto:best",}])
    specialakola6 = CloudinaryField('specialakola6',transformation=[{"quality":"auto:best",}])
    specialakola7 = CloudinaryField('specialakola7',transformation=[{"quality":"auto:best",}])
    specialakola8 = CloudinaryField('specialakola8',transformation=[{"quality":"auto:best",}])

class DailySpecialBuldhana(models.Model):
    buldhanaid = models.AutoField(primary_key=True)
    date =models.DateField(auto_now=False, auto_now_add=False)
    specialbuldhana1  = CloudinaryField('specialakola1',transformation=[{"quality":"auto:best",}])
    specialbuldhana2 = CloudinaryField('specialakola2',transformation=[{"quality":"auto:best",}])
    specialbuldhana3 = CloudinaryField('specialakola3',transformation=[{"quality":"auto:best",}])
    specialbuldhana4 = CloudinaryField('specialakola4',transformation=[{"quality":"auto:best",}])
    specialbuldhana5 = CloudinaryField('specialakola5',transformation=[{"quality":"auto:best",}])
    specialbuldhana6 = CloudinaryField('specialakola6',transformation=[{"quality":"auto:best",}])
    specialbuldhana7 = CloudinaryField('specialakola7',transformation=[{"quality":"auto:best",}])
    specialbuldhana8 = CloudinaryField('specialakola8',transformation=[{"quality":"auto:best",}])

# yesterday = datetime.now()
# date =  datetime.strftime(yesterday, '%Y-%m-%d')

class PageOneClip(models.Model):
    page_date =models.DateField(auto_now=False, auto_now_add=False)
    clip_one = CloudinaryField('clip_one',transformation=[{"quality":"auto:best",}])
    clip_two = CloudinaryField('clip_two',transformation=[{"quality":"auto:best",}])
    clip_three = CloudinaryField('clip_three',transformation=[{"quality":"auto:best",}])
    clip_four = CloudinaryField('clip_four',transformation=[{"quality":"auto:best",}])
    clip_five = CloudinaryField('clip_five',transformation=[{"quality":"auto:best",}])
    clip_six = CloudinaryField('clip_six',transformation=[{"quality":"auto:best",}])
    clip_seven = CloudinaryField('clip_seven',transformation=[{"quality":"auto:best",}])
    clip_eight = CloudinaryField('clip_eight',transformation=[{"quality":"auto:best",}])
    clip_nine = CloudinaryField('clip_nine',transformation=[{"quality":"auto:best",}])


class PageTwoClip(models.Model):
    page_two_date = models.DateField(auto_now=False, auto_now_add=False)
    two_clip_one = CloudinaryField('two_clip_one',transformation=[{"quality":"auto:best",}])
    two_clip_two = CloudinaryField('two_clip_two',transformation=[{"quality":"auto:best",}])
    two_clip_three = CloudinaryField('two_clip_three',transformation=[{"quality":"auto:best",}])
    two_clip_four = CloudinaryField('two_clip_four',transformation=[{"quality":"auto:best",}])
    two_clip_five = CloudinaryField('two_clip_five',transformation=[{"quality":"auto:best",}])
    two_clip_six = CloudinaryField('two_clip_six',transformation=[{"quality":"auto:best",}])
    two_clip_seven = CloudinaryField('two_clip_six',transformation=[{"quality":"auto:best",}])
    two_clip_eight = CloudinaryField('two_clip_eight',transformation=[{"quality":"auto:best",}])
    two_clip_nine = CloudinaryField('two_clip_nine',transformation=[{"quality":"auto:best",}])
    two_clip_ten = CloudinaryField('two_clip_ten',transformation=[{"quality":"auto:best",}])


class Clipping(models.Model):
    id = models.AutoField(primary_key=True)
    clipdate =models.DateField(auto_now_add=True)
    today = date.today()
    d = today.strftime("%d-%m-%Y")
    abc =  datetime.today().strftime("%Y/%m/%d")
    clipimage = CloudinaryField('clipimage',folder = '{}'.format(abc) ,overwrite=True,transformation=[{"quality":"auto:eco", "height": 1210, "crop": "lpad", "background":"white"},{'overlay': "ajinkya", 'width': "1.0", 'height': "1.0", 'gravity': "north",},{'overlay' :{ 'font_family': "Arial", 'font_size': 35,'font_weight': "bold", 'text': "{}".format(d)},'gravity': "north",'y':90},{"flags":"attachment:ajinkyabharat"}])

class TopAdds(models.Model):
    add_date =  models.DateField(auto_now=False, auto_now_add=False)
    add_one = CloudinaryField('two_clip_one',transformation=[{"quality":"auto:best",}])
    add_two = CloudinaryField('two_clip_one',transformation=[{"quality":"auto:best",}])

class BottomAdds(models.Model):
    bottom_add_date =  models.DateField(auto_now=False, auto_now_add=False)
    bottom_add_one = CloudinaryField('two_clip_one',transformation=[{"quality":"auto:best",}])
    bottom_add_two = CloudinaryField('two_clip_one',transformation=[{"quality":"auto:best",}])

class AdvertisementForm(models.Model):
    client_name =  models.CharField( max_length=100)
    client_address =  models.CharField( max_length=200)
    client_number =  models.CharField( max_length=15)
    client_agent_name =  models.CharField( max_length=100)

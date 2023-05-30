from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_photo = models.ImageField(null=True, blank=True,upload_to='images/')
    follows = models.ManyToManyField('self',related_name='followed_by',blank=True,symmetrical=False)
    update = models.DateTimeField(User,auto_now=True)
    def __str__(self):
        return self.user.username

class Twitt(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='twitt')
    published = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=250)
    like = models.ManyToManyField(User,related_name='liketwitt')
    
    def likes_count(self):
        return self.like.count()
    
    def __str__(self):
        return (
            f'{self.user}'
            f'({self.published:%Y-%m-%d %H:M}):'
            f'{self.body}...'
            )
    def get_absolute_url(self):
        return reverse("Twitt:individoual_twitt")
    


def create_profile(created, instance, sender, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile,sender=User)

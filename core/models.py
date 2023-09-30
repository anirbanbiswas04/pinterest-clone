from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def get_bio(self):
        if self.bio:
            return self.bio
        return 'No bio is set.'

from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from .utils import make_thumbnail


class Pin(models.Model):
    created_by = models.ForeignKey(get_user_model(), related_name='pins', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pins', null=False, blank=False)
    thumbnail = models.ImageField(upload_to='pins/thumbnails', null=True, blank=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.created_by.username + ' - ' + str(self.created_at)
    
    def get_total_like(self):
        no_of_likes = Pin.objects.filter(id=self.id).annotate(number=models.Count('likes')).distinct()
        return no_of_likes[0].number    
    
    def save(self, *args, **kwargs):
        if self.image:
            self.thumbnail = make_thumbnail(self.image)

        return super(Pin, self).save(*args, **kwargs)
    

class Like(models.Model):
    pin = models.ForeignKey(Pin, related_name='likes', on_delete=models.CASCADE)
    like_by = models.ForeignKey(get_user_model(), related_name='likes', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.pin} by {self.like_by.get_username}"

    
    
    



from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    bio = models.TextField()
    pic = models.ImageField(upload_to='profiles/')
    user = models.OneToOneField(User,blank=True, on_delete=models.CASCADE, related_name="profile")

    def post_save_user_model(sender, instance, created, *args, **kwargs):
        if created:
            try:
                Profile.objects.create(user=instance)
            except:
                pass
    post_save.connect(post_save_user_model, sender=settings.AUTH_USER_MODEL)

    def __str__(self):
        return str(self.user)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    description = models.CharField(max_length=30)
    post_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    likes = models.CharField(max_length=30)
    comments = models.TextField()
    pic = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.description

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.delete()

    @classmethod
    def get_image_by_id(id):
        img = Image.objects.get(id)
        return img


class Like(models.Model):
    liked = models.ForeignKey(Image, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    @classmethod
    def likes(cls, img, prfl):
        like = cls(liked=img, liked_by=prfl)
        return like.save()

    def delete_like(self):
        self.delete()

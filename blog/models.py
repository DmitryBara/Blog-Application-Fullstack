import os
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# import locale
# locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


# it's not necessery now because I load image to AWS
# save in MEDIA_ROOT/article-img/...
def get_image_path(instance, filename):
    return os.path.join('articles-img', instance.uuid, filename)


class Article(models.Model):
    uuid = models.CharField(max_length=50, default='None')
    title = models.CharField(max_length=50, db_index=True)
    text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(null=True, auto_now_add=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="art_to_likes")
    hiden = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_url(self):
        return "/{}/".format(self.id)

    def ru_date(self):
        return ((self.pub_date + timedelta(hours=3)).strftime("%d %B %Y %H:%M"))

    def src_aws(self):
        return ("https://mysite1-bucket.s3.amazonaws.com/" + self.uuid)
















# class Tag(models.Model):


# class Answer(models.Model):
#     text = models.TextField(default="")
#     added_at = models.DateField(null=True)
#     question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
#     author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.text

# class Article(models.Model):
#     title = models.CharField(default="", max_length=1024)
#     text = models.TextField(default="")
#     added_at = models.DateField(null=True)    
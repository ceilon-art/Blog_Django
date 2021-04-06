from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comments(models.Model):
    comment_name = models.CharField(
        max_length=250, verbose_name='Nome do comentário')
    comment_email = models.EmailField(verbose_name="Email do comentário")
    comment = models.TextField(verbose_name='Comentário')
    comment_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Post do comentário')
    comment_user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Usuário que comentou')
    comment_data = models.DateField(default=timezone.now, verbose_name='Data')
    comment_published = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self):
        return self.comment_name

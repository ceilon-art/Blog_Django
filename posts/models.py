from django.db import models
from categories.models import Categories
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    post_data = models.DateTimeField(
        default=timezone.now, verbose_name='Data do post')
    post_content = models.TextField(verbose_name='Conteúdo do post')
    post_excert = models.TextField(verbose_name='Excerto')
    post_category = models.ForeignKey(
        Categories, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categorias')
    post_image = models.ImageField(
        upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    post_published = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self):
        return self.title

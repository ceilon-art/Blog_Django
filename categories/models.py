from django.db import models


class Categories(models.Model):
    name_cat = models.CharField(max_length=50, verbose_name='Categoria')

    def __str__(self):
        return self.name_cat

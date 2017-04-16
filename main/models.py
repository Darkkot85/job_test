# -*- coding: utf-8 -*-
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models


class Category(MPTTModel):
    """ Класс Категорий с древовидной структурой   
     При удалении родительской категории все подкатегории тоже удаляются
     Категории отсортированны по id в дереве и уровню вложенности
     
     def __unicode__ -- возвращает название категории
     
     """
    name = models.CharField(max_length=50, verbose_name='Название')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('tree_id', 'level')

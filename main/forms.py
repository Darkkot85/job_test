# -*- coding: utf-8 -*-

from django import forms
from .models import Category


class NewCategoryForm(forms.ModelForm):
    """Класс формы, создающей новую Категорию.
    Используются поля name(название) и parent(родитель, может быть пустым)
    
    """
    class Meta:
        model = Category
        fields = ['name', 'parent']


class CategoryUpdRem(forms.Form):
    """Класс формы, служащей для обновления названия или удаления категории"""
    cat_name = forms.CharField(max_length=50, label='cat_name')

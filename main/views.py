# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView

from .models import Category
from .forms import NewCategoryForm, CategoryUpdRem


def show_category(request, pk):
    """Отображает, переименовывает или удаляет конкретную категорию"""
    current_category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        if 'button_delete' in request.POST:
            current_category.delete()
        elif 'button_rename' in request.POST:
            form = CategoryUpdRem(request.POST)
            if form.is_valid():
                current_category.name = form.cleaned_data['cat_name']
                current_category.save()
        return HttpResponseRedirect("/")
    else:
        root_category_id = current_category.get_root().id
        return render(request, 'main/show_category.html', {'nodes': Category.objects.all(),
                                                           'current_category': current_category,
                                                           'root_category_id': root_category_id})


class MainView(ListView):
    """Вывод и получение данных с главной страницы
    def get_context_data -- Подготовка контекста для вывода дерева категорий и формы
    def post -- Создание новой категории по данным из формы.
    
    """
    model = Category
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['form'] = NewCategoryForm
        context['nodes'] = Category.objects.all()
        return context

    def post(self, request):
        new_category = NewCategoryForm(request.POST)
        if new_category.is_valid():
            new_category.save()
        return HttpResponseRedirect("")

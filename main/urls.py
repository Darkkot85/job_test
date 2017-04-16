from django.conf.urls import url

from .views import MainView, show_category

urlpatterns = [
    url(r'^category/(?P<pk>\d+)/$', show_category, name='show_category'),
    url(r'^', MainView.as_view(), name='main'),
]


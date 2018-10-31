from django.conf.urls import url,include
from . import views as d
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',d.fridge,name='fridge'),
]
from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    # ex: /blog/5/
    path('<int:blog_id>/', views.detail, name='detail'),
]

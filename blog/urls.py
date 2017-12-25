from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    # the 'name' value as called by the {% url %} template tag
    path('<int:post_id>/', views.detail, name='detail'),
]

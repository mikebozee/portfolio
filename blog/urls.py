from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', views.IndexView.as_view(), name='index'),
    # the 'name' value as called by the {% url %} template tag
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]

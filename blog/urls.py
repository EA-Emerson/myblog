from . import views
from django.urls import path


urlpatterns = [
    # path('', views.PostList.as_view(), name="home"),
    path('', views.index, name="home"),
    # path('<slug:slug>/', views.PostList.as_view(), name="post_detail"),
]
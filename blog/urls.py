from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:pk>/', views.DetailBlogView.as_view(), name='detail_blog'),
    path('<int:pk>/like', views.LikeBlog.as_view(), name='like_blog'),
    path('featured/', views.Featured.as_view(), name='featured'),
    path('<int:pk>/delete', views.DeleteBlogView.as_view(), name='delete_blog')
]
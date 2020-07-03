from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name='post'
urlpatterns=[
    path('list/',PostList.as_view(),name='post_list'),
    path('create_post/',CreatePost.as_view(),name='create_post'),
   
    path('detail/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('delete_post/<int:pk>/',DeletePost.as_view(),name='delete_post'),
   
  
    #path('post_edit/<int:pk>/',UpdatePost.as_view(),name='update_post'),
   
    path('editpost/<int:pk>/',EditPost.as_view(),name='edit_post'),
   


]
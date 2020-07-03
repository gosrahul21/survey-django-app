from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView,ListView
from .models import *
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
# Create your views here.




class PostList(LoginRequiredMixin,ListView):
    model=Post
    template_name = 'post/post_list.html'


class CreatePost(LoginRequiredMixin,CreateView):
    form_class=PostForm
    model=Post
    template_name='post/post_create.html'
    success_url = reverse_lazy('post:post_list')


    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        #self.object.image=self.request.FILES['image']
        self.object.save()
        print("**************************************************************************************")
        return super().form_valid(form)

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post
    template_name = 'post/post_detail.html'






class DeletePost(LoginRequiredMixin,DeleteView):
    model=Post
    success_url = reverse_lazy('post:post_list')
    template_name='post/post_delete_confirm.html'






class EditPost(LoginRequiredMixin,UpdateView):
    form_class=PostForm
    model = Post
    template_name='post/post_create.html'
    success_url = reverse_lazy('post:post_list')



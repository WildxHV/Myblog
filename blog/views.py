from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog

class Home(ListView):
	model = Blog
	queryset = Blog.objects.all().order_by('-date')
	template_name = 'blog/home.html'
	paginate_by = 1

class Featured(ListView):
	model = Blog
	queryset = Blog.objects.filter(featured=True).order_by('-date')
	template_name = 'blog/featured.html'
	paginate_by = 1

class DetailBlogView(DetailView):
	model = Blog
	template_name = 'blog/blog_post.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DetailBlogView, self).get_context_data(*args, **kwargs)
		context['liked_by_user'] = False
		blog = Blog.objects.get(id=self.kwargs.get('pk'))
		if blog.likes.filter(pk=self.request.user.id).exists():
			context['liked_by_user'] = True
		return context

class LikeBlog(View):
	def post(self, request, pk):
		blog = Blog.objects.get(id=pk)
		if blog.likes.filter(pk=self.request.user.id).exists():
			blog.likes.remove(request.user.id)
		else:
			blog.likes.add(request.user.id)

		blog.save()
		return redirect('detail_blog', pk)

class DeleteBlogView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Blog
	template_name = 'blog/blog_delete.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		blog = Blog.objects.get(id=self.kwargs.get('pk'))
		return self.request.user.id == blog.author.id
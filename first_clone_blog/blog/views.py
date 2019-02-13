from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#function view decorator of login login_required
from django.contrib.auth.decorators import login_required
#same as the above one but is for class view
from blog.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                UpdateView, DeleteView, )
from blog.models import (Comment,Post)
# Create your views here.

class aboutView(TemplateView):
    template_name = 'aboun=t.html'

class postListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class postDetailView(DetailView):
    model = Post

#postCreate should be authorization by user, so it has to be login reqired
class postCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
#same as the above
class postUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class postDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class draftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')

########################################################
### Post approve
#########################################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

#########################################################
### Comment views
########################################################
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()
    return redirect('post_detail', pk = comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

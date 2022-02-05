from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin, FormView

from blog_hillel.forms import RegisterUserForm, ContactUsForm
from blog_hillel.models import Post, Comment


class Home(TemplateView):
    template_name = "home.html"


class ProfileList(ListView):
    queryset = User.objects.all()
    template_name = "profile_list.html"


class ProfileInfo(DetailView):
    model = User
    template_name = "profile_info.html"


class NewPost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Post
    success_message = 'Author successfully created'
    template_name = "post_create.html"
    fields = ('title', 'descript', 'image', 'is_posted')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()

        return super(NewPost, self).form_valid(form)


class PostList(ListView):
    template_name = "post_list.html"
    queryset = Post.objects.all().filter(is_posted=True)


class PostInfo(DetailView):
    template_name = "post_detail.html"
    model = Post


class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    success_message = 'Author successfully updated'
    success_url = reverse_lazy('post-list')
    login_url = '/admin/'


class PostDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_message = 'Author successfully deleted'
    success_url = reverse_lazy('post-list')
    login_url = '/admin/'


class CommentView(CreateView):
    model = Comment
    template_name = 'comment.html'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register_form.html'
    success_url = reverse_lazy('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login_form.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class MessageAdmin(SuccessMessageMixin, FormView):
    form_class = ContactUsForm
    success_message = 'Message send'
    success_url = reverse_lazy('home')
    template_name = 'contact_us.html'

    def form_valid(self, form):
        data = form.cleaned_data
        send_mail('MESSAGE',
                  data['text'],
                  'Annet2014annet@gmail.com',
                  ['Annet2014annet@gmail.com'],
                  fail_silently=False,
                  )
        return super().form_valid(form)

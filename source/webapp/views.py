from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from webapp.forms import PhotoForm
from webapp.models import Photo


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '')
            if next_url:
                return redirect(next_url)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'registration/login.html', context=context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('webapp:index')


class IndexView(ListView):
    model = Photo
    template_name = 'photo/list.html'
    context_object_name = 'photos'
    queryset = Photo.objects.all()


class PhotoDetailView(DetailView):
    template_name = 'photo/detail.html'
    context_object_name = 'photo'
    model = Photo
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('webapp:photo_detail')


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photo/create.html'
    form_class = PhotoForm
    permission_required = 'webapp.add_photo'
    permission_denied_message = '403 Доступ запрещен'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photo/update.html'
    form_class = PhotoForm
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    pk_kwargs_url = 'pk'
    template_name = 'photo/delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('webapp:photos_view')
    permission_required = 'webapp.delete_photo'
    permission_denied_message = '403 Denied  permission'

    def get_success_url(self):
        return reverse('webapp:index')
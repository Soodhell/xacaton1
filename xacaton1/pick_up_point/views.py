from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .forms import *
from .models import *


class PickUpPointCreate(CreateView):

    template_name = "pick_up_point/create.html"
    form_class = CreatePickUpPointForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить пункт выдачи'
        context['name_title_form'] = 'Добавить пункт выдачи'
        context['name_button'] = 'Добавить'
        return context


class PickUpPointList(ListView):

    template_name = "pick_up_point/list.html"
    model = PickUpPoint
    context_object_name = 'posts'

    def get_queryset(self):
        return PickUpPoint.objects.all().filter(user=self.request.user)
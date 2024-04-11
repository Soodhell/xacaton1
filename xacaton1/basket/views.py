from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .models import *
from .forms import *
from django.shortcuts import redirect


class BasketCreate(LoginRequiredMixin, CreateView):
    template_name = "basket/index.html"
    form_class = CreateBasket

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить публикацию'
        context['name_title_form'] = 'Добавить публикацию'
        context['name_button'] = 'Добавить'
        return context


class BasketUpdate(LoginRequiredMixin, UpdateView):
    template_name = "basket/index.html"
    model = Basket

    fields = ['count',]

    def get_success_url(self):
        return reverse_lazy('main')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if (self.request.user == self.object.user):
            return super().get(request, *args, **kwargs)

        return redirect('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование публикации'
        context['name_title_form'] = 'Редактировать публикацию'
        context['name_button'] = 'Редактировать'
        return context


class BasketDetail(LoginRequiredMixin, DetailView):
    template_name = "basket/detail.html"
    model = Basket
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Публикация'
        context['name_title_form'] = 'Ваша публикация!'
        return context


class BasketlineList(LoginRequiredMixin, ListView):
    template_name = "basket/basket_line.html"
    model = Basket

    def get_queryset(self):
        return Basket.objects.all().filter(user=self.request.user)

    extra_context = {'title': 'Статьи'}

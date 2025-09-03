from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class ExameListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Exame
    template_name = 'exame_list.html'
    context_object_name = 'exames'
    paginate_by = 10
    permission_required = 'exames.view_exame'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class ExameCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Exame
    template_name = 'exame_create.html'
    form_class = forms.ExameForm
    success_url = reverse_lazy('exame_list')
    permission_required = 'exames.add_exame'


class ExameDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Exame
    template_name = 'exame_detail.html'
    permission_required = 'exames.view_exame'


class ExameUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Exame
    template_name = 'exame_update.html'
    form_class = forms.ExameForm
    success_url = reverse_lazy('exame_list')
    permission_required = 'exames.change_exame'


class ExameDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Exame
    template_name = 'exame_delete.html'
    success_url = reverse_lazy('exame_list')
    permission_required = 'exames.delete_exame'


class ExameCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Exame.objects.all()
    serializer_class = serializers.ExameSerializer


class ExameRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Exame.objects.all()
    serializer_class = serializers.ExameSerializer

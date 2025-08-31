from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class GrupoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Grupo
    template_name = 'grupo_list.html'
    context_object_name = 'grupos'
    paginate_by = 10
    permission_required = 'grupos.view_grupo'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class GrupoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Grupo
    template_name = 'grupo_create.html'
    form_class = forms.GrupoForm
    success_url = reverse_lazy('grupo_list')
    permission_required = 'grupos.add_grupo'


class GrupoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Grupo
    template_name = 'grupo_detail.html'
    permission_required = 'grupos.view_grupo'


class GrupoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Grupo
    template_name = 'grupo_update.html'
    form_class = forms.GrupoForm
    success_url = reverse_lazy('grupo_list')
    permission_required = 'grupos.change_grupo'


class GrupoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Grupo
    template_name = 'grupo_delete.html'
    success_url = reverse_lazy('grupo_list')
    permission_required = 'grupos.delete_grupo'


class GrupoCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Grupo.objects.all()
    serializer_class = serializers.GrupoSerializer


class GrupoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Grupo.objects.all()
    serializer_class = serializers.GrupoSerializer

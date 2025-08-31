from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class TipoExameListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.TipoExame
    template_name = 'tipoexame_list.html'
    context_object_name = 'tiposexames'
    paginate_by = 10
    permission_required = 'tiposexames.view_tipoexame'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class TipoExameCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.TipoExame
    template_name = 'tipoexame_create.html'
    form_class = forms.TipoExameForm
    success_url = reverse_lazy('tipoexame_list')
    permission_required = 'tiposexames.add_tipoexame'


class TipoExameDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.TipoExame
    template_name = 'tipoexame_detail.html'
    permission_required = 'tiposexames.view_tipoexame'


class TipoExameUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.TipoExame
    template_name = 'tipoexame_update.html'
    form_class = forms.TipoExameForm
    success_url = reverse_lazy('tipoexame_list')
    permission_required = 'tiposexames.change_tipoexame'


class TipoExameDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.TipoExame
    template_name = 'tipoexame_delete.html'
    success_url = reverse_lazy('tipoexame_list')
    permission_required = 'tiposexames.delete_tipoexame'


class TipoExameCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.TipoExame.objects.all()
    serializer_class = serializers.TipoExameSerializer


class TipoExameRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TipoExame.objects.all()
    serializer_class = serializers.TipoExameSerializer

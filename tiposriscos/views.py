from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class TipoRiscoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.TipoRisco
    template_name = 'tiporisco_list.html'
    context_object_name = 'tiposriscos'
    paginate_by = 10
    permission_required = 'tiposriscos.view_tiporisco'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class TipoRiscoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.TipoRisco
    template_name = 'tiporisco_create.html'
    form_class = forms.TipoRiscoForm
    success_url = reverse_lazy('tiporisco_list')
    permission_required = 'tiposriscos.add_tiporisco'


class TipoRiscoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.TipoRisco
    template_name = 'tiporisco_detail.html'
    permission_required = 'tiposriscos.view_tiporisco'


class TipoRiscoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.TipoRisco
    template_name = 'tiporisco_update.html'
    form_class = forms.TipoRiscoForm
    success_url = reverse_lazy('tiporisco_list')
    permission_required = 'tiposriscos.change_tiporisco'


class TipoRiscoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.TipoRisco
    template_name = 'tiporisco_delete.html'
    success_url = reverse_lazy('tiporisco_list')
    permission_required = 'tiposriscos.delete_tiporisco'


class TipoRiscoCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.TipoRisco.objects.all()
    serializer_class = serializers.TipoRiscoSerializer


class TipoRiscoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TipoRisco.objects.all()
    serializer_class = serializers.TipoRiscoSerializer

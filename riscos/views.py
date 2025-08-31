from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class RiscoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Risco
    template_name = 'risco_list.html'
    context_object_name = 'riscos'
    paginate_by = 10
    permission_required = 'riscos.view_risco'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class RiscoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Risco
    template_name = 'risco_create.html'
    form_class = forms.RiscoForm
    success_url = reverse_lazy('risco_list')
    permission_required = 'riscos.add_risco'


class RiscoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Risco
    template_name = 'risco_detail.html'
    permission_required = 'riscos.view_risco'


class RiscoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Risco
    template_name = 'risco_update.html'
    form_class = forms.RiscoForm
    success_url = reverse_lazy('risco_list')
    permission_required = 'riscos.change_risco'


class RiscoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Risco
    template_name = 'risco_delete.html'
    success_url = reverse_lazy('risco_list')
    permission_required = 'riscos.delete_risco'


class RiscoCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Risco.objects.all()
    serializer_class = serializers.RiscoSerializer


class RiscoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Risco.objects.all()
    serializer_class = serializers.RiscoSerializer

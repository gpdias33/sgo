from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class FuncaoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Funcao
    template_name = 'funcao_list.html'
    context_object_name = 'funcoes'
    paginate_by = 10
    permission_required = 'funcoes.view_funcao'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class FuncaoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Funcao
    template_name = 'funcao_create.html'
    form_class = forms.FuncaoForm
    success_url = reverse_lazy('funcao_list')
    permission_required = 'funcoes.add_funcao'


class FuncaoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Funcao
    template_name = 'funcao_detail.html'
    permission_required = 'funcoes.view_funcao'


class FuncaoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Funcao
    template_name = 'funcao_update.html'
    form_class = forms.FuncaoForm
    success_url = reverse_lazy('funcao_list')
    permission_required = 'funcoes.change_funcao'


class FuncaoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Funcao
    template_name = 'funcao_delete.html'
    success_url = reverse_lazy('funcao_list')
    permission_required = 'funcoes.delete_funcao'


class FuncaoCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Funcao.objects.all()
    serializer_class = serializers.FuncaoSerializer


class FuncaoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Funcao.objects.all()
    serializer_class = serializers.FuncaoSerializer

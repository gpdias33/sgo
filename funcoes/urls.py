from django.urls import path
from . import views


urlpatterns = [
    path('funcoes/list/', views.FuncaoListView.as_view(), name='funcao_list'),
    path('funcoes/create/', views.FuncaoCreateView.as_view(), name='funcao_create'),
    path('funcoes/<int:pk>/detail/', views.FuncaoDetailView.as_view(), name='funcao_detail'),
    path('funcoes/<int:pk>/update/', views.FuncaoUpdateView.as_view(), name='funcao_update'),
    path('funcoes/<int:pk>/delete/', views.FuncaoDeleteView.as_view(), name='funcao_delete'),

    path('api/v1/funcoes/', views.FuncaoCreateListAPIView.as_view(), name='funcao-create-list-api-view'),
    path('api/v1/funcoes/<int:pk>/', views.FuncaoRetrieveUpdateDestroyAPIView.as_view(), name='funcao-detail-api-view'),
]

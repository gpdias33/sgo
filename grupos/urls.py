from django.urls import path
from . import views


urlpatterns = [
    path('grupos/list/', views.GrupoListView.as_view(), name='grupo_list'),
    path('grupos/create/', views.GrupoCreateView.as_view(), name='grupo_create'),
    path('grupos/<int:pk>/detail/', views.GrupoDetailView.as_view(), name='grupo_detail'),
    path('grupos/<int:pk>/update/', views.GrupoUpdateView.as_view(), name='grupo_update'),
    path('grupos/<int:pk>/delete/', views.GrupoDeleteView.as_view(), name='grupo_delete'),

    path('api/v1/grupos/', views.GrupoCreateListAPIView.as_view(), name='grupo-create-list-api-view'),
    path('api/v1/grupos/<int:pk>/', views.GrupoRetrieveUpdateDestroyAPIView.as_view(), name='grupo-detail-api-view'),
]

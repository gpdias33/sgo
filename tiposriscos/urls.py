from django.urls import path
from . import views


urlpatterns = [
    path('tiposriscos/list/', views.TipoRiscoListView.as_view(), name='tiporisco_list'),
    path('tiposriscos/create/', views.TipoRiscoCreateView.as_view(), name='tiporisco_create'),
    path('tiposriscos/<int:pk>/detail/', views.TipoRiscoDetailView.as_view(), name='tiporisco_detail'),
    path('tiposriscos/<int:pk>/update/', views.TipoRiscoUpdateView.as_view(), name='tiporisco_update'),
    path('tiposriscos/<int:pk>/delete/', views.TipoRiscoDeleteView.as_view(), name='tiporisco_delete'),

    path('api/v1/tiposriscos/', views.TipoRiscoCreateListAPIView.as_view(), name='tiporisco-create-list-api-view'),
    path('api/v1/tiposriscos/<int:pk>/', views.TipoRiscoRetrieveUpdateDestroyAPIView.as_view(), name='tiporisco-detail-api-view'),
]

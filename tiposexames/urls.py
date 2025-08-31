from django.urls import path
from . import views


urlpatterns = [
    path('tiposexames/list/', views.TipoExameListView.as_view(), name='tipoexame_list'),
    path('tiposexames/create/', views.TipoExameCreateView.as_view(), name='tipoexame_create'),
    path('tiposexames/<int:pk>/detail/', views.TipoExameDetailView.as_view(), name='tipoexame_detail'),
    path('tiposexames/<int:pk>/update/', views.TipoExameUpdateView.as_view(), name='tipoexame_update'),
    path('tiposexames/<int:pk>/delete/', views.TipoExameDeleteView.as_view(), name='tipoexame_delete'),

    path('api/v1/tiposexames/', views.TipoExameCreateListAPIView.as_view(), name='tipoexame-create-list-api-view'),
    path('api/v1/tiposexames/<int:pk>/', views.TipoExameRetrieveUpdateDestroyAPIView.as_view(), name='tipoexame-detail-api-view'),
]

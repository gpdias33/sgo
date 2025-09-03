from django.urls import path
from . import views


urlpatterns = [
    path('exames/list/', views.ExameListView.as_view(), name='exame_list'),
    path('exames/create/', views.ExameCreateView.as_view(), name='exame_create'),
    path('exames/<int:pk>/detail/', views.ExameDetailView.as_view(), name='exame_detail'),
    path('exames/<int:pk>/update/', views.ExameUpdateView.as_view(), name='exame_update'),
    path('exames/<int:pk>/delete/', views.ExameDeleteView.as_view(), name='exame_delete'),

    path('api/v1/exames/', views.ExameCreateListAPIView.as_view(), name='exame-create-list-api-view'),
    path('api/v1/exames/<int:pk>/', views.ExameRetrieveUpdateDestroyAPIView.as_view(), name='exame-detail-api-view'),
]

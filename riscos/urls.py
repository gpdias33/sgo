from django.urls import path
from . import views


urlpatterns = [
    path('riscos/list/', views.RiscoListView.as_view(), name='risco_list'),
    path('riscos/create/', views.RiscoCreateView.as_view(), name='risco_create'),
    path('riscos/<int:pk>/detail/', views.RiscoDetailView.as_view(), name='risco_detail'),
    path('riscos/<int:pk>/update/', views.RiscoUpdateView.as_view(), name='risco_update'),
    path('riscos/<int:pk>/delete/', views.RiscoDeleteView.as_view(), name='risco_delete'),

    path('api/v1/riscos/', views.RiscoCreateListAPIView.as_view(), name='risco-create-list-api-view'),
    path('api/v1/riscos/<int:pk>/', views.RiscoRetrieveUpdateDestroyAPIView.as_view(), name='risco-detail-api-view'),
]

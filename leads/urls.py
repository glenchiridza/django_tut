from django.urls import path
from .views import (lead_list, lead_detail, lead_update, lead_delete
, LeadListView, LeadDetailView, LeadCreateView,LeadDeleteView,LeadUpdateView)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(),name='lead-list'),
    path('create/', LeadCreateView, name='lead-create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView, name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView, name='lead-delete')
]
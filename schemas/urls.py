from django.urls import path
from . import views

urlpatterns = [
    path('create_schema/', views.SchemaCreateView.as_view(), name='SchemaCreateView'),
    path('schemas_list/', views.SchemaListView.as_view(), name='SchemaListView'),
]

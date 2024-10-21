from django.urls import path
from .views import dashboard_view, upload_file_view, login_view, logout_view, delete_file_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),  # This should match the root URL
    path('upload/', upload_file_view, name='upload_file'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('delete/<int:file_id>/', delete_file_view, name='delete_file'),
]

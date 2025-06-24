from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.Home_page, name='Home_page'), 
    path('Civil_Engineering.html', views.Civil_Engineering, name='Civil_Engineering'),
    path('Computer_Engineering.html', views.Computer_Engineering, name='Computer_Engineering'),
    path('Mechanical_Engineering.html', views.Mechanical_Engineering, name='Mechanical_Engineering'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('upload_success/', views.upload_success, name = 'upload_success'),
    path('download_file/<str:branch>/<int:semester>/<str:subject_code>/<str:subject_name>/<str:material_type>', views.download_file, name='download_file'),
    path('list_files/', views.list_files, name='list_files'),
    path('study_moment_gallery/', views.study_moment_gallery, name='study_moment_gallery'),
    path('upload_study_moment/', views.upload_study_moment, name='upload_study_moment'),
    
   ] 
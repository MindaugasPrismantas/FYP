from django.conf import settings
from django.contrib import admin
from django.urls import path
from pages.views import home_view, upload_view, file_list_view
from files.views import delete_file
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view),
    path('home', home_view, name='home'),
    path('upload/', upload_view, name='upload'),
    path('file/', file_list_view, name='file_list'),
    path('file/<int:pk>/', delete_file, name='delete_file'),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Hello properties Administration"
admin.site.site_title ="Administartion"
admin.site.index_title= "Welcome To  Hello Properties Administration"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('realapp.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

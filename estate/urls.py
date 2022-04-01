from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static


urlpatterns = [
    path('supersecret/', admin.site.urls),
    path('api/v1/auth/',include('djoser.urls')),
    path('api/v1/auth/',include('djoser.urls.jwt')),
    path('api/v1/profile/',include("apps.profiles.urls")),
    path('api/v1/properties/',include("apps.properties.urls")),
    path('api/v1/ratings/',include('apps.ratings.urls')),
    path("api/v1/enquiries/",include('apps.enquiries.urls'))
] 

admin.site.site_header = "Estate Admin"
admin.site.site_title = "Estate ADmin Portal"
admin.site.index_title = "Welcome to the Estate Portal"

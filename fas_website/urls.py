from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),  # В папке homepage лежит файл urls
    path('enroll/', include('enrollment.urls')),
    path('test_movies/', include('test_movies.urls'))
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:  # Если дебаг включен
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




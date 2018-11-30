from django.contrib import admin
from django.urls import include,path
from DjangoUeditor import urls as DjiangoUditorUrls
from django.conf import settings

urlpatterns = [
    path('', include('polls.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('ueditor/',include(DjiangoUditorUrls)),
    path('search/', include('haystack.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

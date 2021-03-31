
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


from news_api import urls
from  news_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('student_profile.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('authentication.urls')),
    path('news/',include('news_api.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

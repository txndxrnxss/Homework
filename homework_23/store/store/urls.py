from django.contrib import admin
from django.urls import path, include
import store_games.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store_games/', include('store_games.urls')),
] 




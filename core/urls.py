from aladdinprecos import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('precos/', views.get_precos, name='get_precos'),
]

handler404 = views.handler404


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('poll.urls')),
    path('assignment/',include('coarse.urls')),
    path("classbasedview/", include('class_based_view.urls')),
    path('mixinsapi/',include('mixins_api.urls')),
    path('viewsetapi/',include('viewset_api.urls')),
    path('nsapp/',include('nsapp.urls'))
]

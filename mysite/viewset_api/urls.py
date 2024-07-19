from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import Coarse ,index
router = DefaultRouter()
router.register('coarses', Coarse, basename='coarse' )

urlpatterns = [
    path('',index),
    path('',include(router.urls))
]

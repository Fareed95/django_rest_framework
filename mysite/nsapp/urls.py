from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import InstructorView, CoarseView

router = DefaultRouter()
router.register('instructor',InstructorView,basename='instructor')


urlpatterns = [
    path('coarse',CoarseView.as_view()),
    path('',include(router.urls))
]

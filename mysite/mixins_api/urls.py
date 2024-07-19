from django.urls import path
from .views import index , CoarseList, CoarseDetailview
urlpatterns = [
    path('', index),
    path('coarses',CoarseList.as_view()),
    path('coarses/<int:pk>',CoarseDetailview.as_view())

]

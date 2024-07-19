from django.urls import path
from . views import index, CoarseView,Coarse_personal

urlpatterns = [
    path("",index, name = "index"),
    path("coarse",CoarseView),
    path("coarse/<int:pk>",Coarse_personal)
]

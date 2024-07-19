from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, mixins
from .models import Coarse
from .serializers import CoarseSerializer

def index(request):
    return HttpResponse("zindagi kya khud khuda hai shaida tumhara ... akaaa lelo sallam ab hamara ")

# class CoarseList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Coarse.objects.all()
#     serializer_class = CoarseSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)

# class CoarseDetailview(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Coarse.objects.all()
#     serializer_class = CoarseSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)
    
#     def put(self, request, pk):
#         return self.update(request, pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)


class CoarseList(generics.ListCreateAPIView):
    queryset = Coarse.objects.all()
    serializer_class = CoarseSerializer

class CoarseDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coarse.objects.all()
    serializer_class = CoarseSerializer



# ooh bhai maza aagaya .. itna bada code chota hogaya maaannnnnnn
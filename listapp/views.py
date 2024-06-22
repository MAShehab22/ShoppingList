from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'listapp/index.html')


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

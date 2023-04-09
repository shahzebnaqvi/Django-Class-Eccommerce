from django.shortcuts import render
from rest_framework.decorators import api_view
from cartitem.models import CartItem
from cartitem.serializers import CartItemSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['Get'])
def cartview(request):
    queryset = CartItem.objects.all()
    serializer = CartItemSerializer(queryset,many=True)
    return Response({'status':200,'payload':serializer.data})

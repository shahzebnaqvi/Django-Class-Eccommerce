from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from products.serializers import ProductSerializer
from products.models import Product

# Create your views here.
class ListProductAPIView(ListAPIView):
    """This endpoint list all of the available Products from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UpdateProductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Product by passing in the id of the Product to update"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DeleteProductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Product from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



































def index(request):

    htmpage='''<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
  <tr>
    <td>Ernst Handel</td>
    <td>Roland Mendel</td>
    <td>Austria</td>
  </tr>
  <tr>
    <td>Island Trading</td>
    <td>Helen Bennett</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Laughing Bacchus Winecellars</td>
    <td>Yoshi Tannamuri</td>
    <td>Canada</td>
  </tr>
  <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td>Giovanni Rovelli</td>
    <td>Italy</td>
  </tr>
</table>'''
    return HttpResponse(htmpage)
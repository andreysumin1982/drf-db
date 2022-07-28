import random
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import encodeTest
from .serializers import encodeTest2
from .serializers import Carsserialiser
from .models import Brand
from .serializers import encodeDataclass
from .mydataset import main
# Create your views here.

#
def index(request):
    if (request.method == 'GET'):
        return render(request, 'drf_api/index.html')
#
def testApi(request):
    if (request.method == 'GET'):
        return HttpResponse(encodeTest(), content_type='application/json')
#
def testApi2(request):
    if (request.method == 'GET'):
        arrlist = [random.randint(1,1000) for j in range(random.randrange(1000))]
        return HttpResponse(encodeTest2(random.randrange(100), arrlist), content_type='application/json')
#
class CarsAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = Carsserialiser
#
def datasetAPI(request):
    if (request.method == 'GET'):
        for key, value in main.dataset1().items():
            #print(value)
            return HttpResponse(encodeDataclass(key, value), content_type='application/json')
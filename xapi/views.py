from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Itemserializers
from base.models import item

@api_view(['GET'])
def xapi(request):
    api_url = {
            'create':'/xapi/create',
            'details':'/xapi/details/<str:pk>/',
            'itemlist':'/xapi/itemlist',
            'update': '/xapi/update/<str:pk>/',
            'delete':'/xapi/delete/<str:pk>/'
          }
    return Response(api_url)

@api_view(['POST'])
def create(request):
    serializer = Itemserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def itemlist(request):
    items =item.objects.all()
    serializer = Itemserializers(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def details(request,pk):
    items =item.objects.get(pk=pk)
    serializer = Itemserializers(items, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def update(request,pk):
    items =item.objects.get(pk=pk)
    serializer = Itemserializers(instance=items,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['delete'])
def delete(request,pk):
    items =item.objects.get(pk=pk)
    items.delete()
   
    return Response('you successfully delete the item')
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Itemserialize
from base.models  import item

@api_view(['GET'])
def getdata(request):
    items = {
        'welcome':'welcome to xapi https://crud-api-a61z.onrender.com/xapi/'
    }
    return Response(items)




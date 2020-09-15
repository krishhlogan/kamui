
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import ipfshttpclient
from .models import  *
import  os

# Create your views here.


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def store_file(request):
    try:
        if 'file' in request.FILES:
            print(request.FILES)
            myfile = IPFSFile()
            myfile.name = request.FILES['file'].name
            # api = ipfshttpclient.connect()
            url = os.environ['URL']
            api = ipfshttpclient.connect(addr='/dns/'+url+'/tcp/5001')
            res = api.add(request.FILES['file'])
            myfile.ipfs_hash = res.as_json()
            myfile.save()
            return Response({'status':'success','error_code':'KM00','resp':res})
        else:
            return Response({'status':'failed','error_code':'KM001'})
    except Exception as e:
        print(e)
        return Response({'status':'failed','error_code':'FS99','error':str(e)})

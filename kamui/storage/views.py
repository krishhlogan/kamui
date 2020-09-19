
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import ipfshttpclient
from .models import  *
import os
import requests
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
            print('/dns/'+url+'/tcp/5001/https')
            api = ipfshttpclient.connect(addr='/dns/'+url+'/tcp/5001/https')
            res = api.add(request.FILES['file'])
            myfile.ipfs_hash = res.as_json()
            myfile.save()
            return Response({'status':'success','status_code':'KM00','resp':res})
        else:
            return Response({'status':'failed','status_code':'KM01'})
    except Exception as e:
        print(e)
        return Response({'status':'failed','status_code':'KM99','error':str(e)})


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def get_file(request):
    try:
        if 'content_hash' in request.POST:
            print(request.POST['content_hash'])
            content_hash = request.POST['content_hash']
            URL = os.environ['IPFS_GATEWAY']+'/{}'.format(content_hash)
            print(URL)
            resp = {'access_url':URL}
            return Response({'status':'success','status_code':'KM00','resp':resp})
        else:
            return Response({'status':'failed','status_code':'KM01','error':'no content hash is sent in post'})
    except Exception as e:
        return Response({'status':'failed','status_code':'KM99','error':str(e)})

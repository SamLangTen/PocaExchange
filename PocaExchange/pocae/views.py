from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pocae.models import PostcardPair
from pocae.serializers import PostcardPairSerializer

# Create your views here.


@csrf_exempt
def pcpair_list(request):
    if request.method == 'GET':
        pairs = PostcardPair.objects.all()
        serializer = PostcardPairSerializer(pairs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        #data = JSONParser.parse(request.body)
        data = JSONParser().parse(request)
        #data = json.loads(request.body)
        #return HttpResponse(request.body())
        serializer = PostcardPairSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

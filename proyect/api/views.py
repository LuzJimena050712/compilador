import json
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

#Importamos nuestro método
from .utills import run_code

@api_view(['POST'])

def main(request):
    if request.method != 'POST':
        return JsonResponse(
            {'code':''},
            status=405   
        )
    
    try:
        #Parseamos el cuerpo de la petición con un Json
        body = request.body.decorate('utf-8') if request.body else ''
        data = json.loads(body) if body else {}
    except Exception:
        return JsonResponse(
            {'code':'Json invalido'},
            status=405
        )
    #Del Json obtenemos el que tenga 'text'
    code = data.get('text','')

    #Ejecutamos las instrucciones con el método que definimos
    output = run_code(code)
    #Da un respuesta de tipo Json
    return Response(
        {"output":output},
        status=status.HTTP_200_OK
    )
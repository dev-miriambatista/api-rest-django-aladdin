import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter(
            'data',
            openapi.IN_QUERY,
            description="Data para consulta dos preços (formato: YYYY-MM-DD)",
            type=openapi.TYPE_STRING
        )
    ]
)
@api_view(['GET'])
def get_precos(request):
    data_req = request.GET.get('data')
    try:
        response = requests.get(
            "https://testedefensoriapr.pythonanywhere.com/precos",
            params={"data": data_req}
        )
        data = response.json()
        return Response({
            "data": data_req,
            "precos": data
        })
    except requests.RequestException as e:
        return Response({"erro": "Informação indisponível no momento, tente mais tarde"}, status=500)


def handler404(request, exception):
    return JsonResponse(
        {"erro": "Endereço não encontrado, verifique se o endereço está correto"},
        status=404,
        json_dumps_params={"ensure_ascii": False}
    )
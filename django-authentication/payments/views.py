import mercadopago 
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PaymentsWithMercadoPago(APIView):
  def post(self, request):
    mercadopago_sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

    preference_data = {
      "items": [
        {
          "title": request.data.get("title"),
          "quantity": int(request.data.get("quantity")),
          "currency_id": "PEN",
          "unit_price": float(request.data.get("unit_price"))
        }
      ],

      "back_urls": {
        "success": "http://localhost:5174/?status=success",
        "failure": "http://localhost:5174/?status=failure",
        "pending": "http://localhost:5174/?status=pending",
      },

      # Para que cuando termine el pago, vuelva a de inmediato a una de las 3 
      # opciones que existen en back_url
      "auto_return": "approved"
    }

    preference_response = mercadopago_sdk.preference().create(preference_data)
    preference_id = preference_response["response"]

    return Response({
      "preference_id": preference_id
    }, status.HTTP_201_CREATED)
  

  
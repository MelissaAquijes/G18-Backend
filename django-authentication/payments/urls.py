from django.urls import path
from .views import PaymentsWithMercadoPago

urlpatterns = [
  path(r'create-preference/', PaymentsWithMercadoPago.as_view(),
        name='mercadopago-create-preference')
]
from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import PaymentListViewSet

app_name = PaymentsConfig.name

urlpatterns = [
    path('payments/', PaymentListViewSet.as_view(), name='payments-list')
]
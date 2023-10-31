from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentListViewSet(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['date',]
    permission_classes = [IsAuthenticated]

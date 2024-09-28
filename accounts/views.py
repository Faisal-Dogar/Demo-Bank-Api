from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, Customer, Transaction
from .serializers import CustomerSerializer,AccountSerializer, TransactionSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer 
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer   

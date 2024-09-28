from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet,CustomerViewSet, TransactionViewSet

router = DefaultRouter()

router.register(r'customers', CustomerViewSet)
router.register(r'accounts', TransactionViewSet)
router.register(r'transaction', AccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

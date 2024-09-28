from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Account(models.Model):
    customer = models.ForeignKey(Customer, related_name='account', 
                                 on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Account{self.account_number}-{self.customer}"
    
    
class Transaction(models.Model):
     account = models.ForeignKey(Customer, related_name='transaction', 
                                 on_delete=models.CASCADE)
     amount = models.DecimalField(max_digits=15, decimal_places=2)
     transaction_type = models.CharField(max_length=10)
     date = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return f"Transaction{self.id}-{self.transaction_type}"
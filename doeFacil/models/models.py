from django.db import models
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from utils import validators
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from uuid import uuid4


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=80, unique=True, null=False)
    password = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator()], unique=True,null=False)
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, null=False, blank=True, default='')
    document = models.CharField(
        max_length=14, unique=True, null=False, validators=[validators.validador_cpf_ou_cnpj],blank=True)
    type_document = models.CharField(max_length=1, null=False)
    birth_date = models.DateField(null=False,blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='doeFacil/photo/images/', null=True, blank=True)
    
    def clean(self):
        if len(self.documento_identificacao) == 11:
            self.type_document = 1
        elif len(self.documento_identificacao) == 14:
            self.type_document = 2
        else:
            raise ValidationError('O valor inserido deve ter 11(CPF) ou 14(CNPJ) digitos válidos.')
        

class Donation_item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_quantity = models.IntegerField()
    open_quantity = models.IntegerField()


class Donation(models.Model):
    user_donation_request = models.IntegerField()
    description = models.TextField()
    donation_item = models.ForeignKey(Donation_item, on_delete=models.CASCADE)
    donation_user_id_request = models.IntegerField()
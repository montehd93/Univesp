from django.db import models
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
    id = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=80, unique=True, null=False)
    password = models.CharField(max_length=255)
    email = models.EmailField(
        validators=[EmailValidator()], max_length=150, unique=True, null=False
    )
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, null=False, blank=True, default="")
    document = models.CharField(
        max_length=11,
        unique=True,
        null=False,
        validators=[validators.validador_cpf_ou_cnpj],
        blank=True,
    )
    type_document = models.CharField(max_length=1, null=False)
    birth_date = models.DateField(null=False, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="doeFacil/photo/images/", null=True, blank=True)

    def clean(self):
        if len(self.documento_identificacao) == 11:
            self.type_document = 1
        else:
            raise ValidationError("O valor inserido deve ter 11(CPF) digitos válidos.")


class Users_Organizations(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # organization_id =


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=255, unique=True, null=False)
    trading_name = models.CharField(max_length=255, unique=True, null=False)
    document = models.CharField(
        max_length=11,
        unique=True,
        null=False,
        validators=[validators.validador_cpf_ou_cnpj],
        blank=True,
    )
    description = models.TextField()
    incorporation_date = models.DateTimeField(auto_now_add=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def clean(self):
        if len(self.documento_identificacao) == 14:
            self.type_document = 2
        else:
            raise ValidationError("O valor inserido deve ter 14(CNPJ) digitos válidos.")

class Organization_Address(models.Model):
    id = models.AutoField(primary_key=True)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255, null=False)
    address_number = models.CharField(max_length=20)
    city = models.CharField(max_length=255, null=False)
    neighborhood = models.CharField(max_length=255, null=False)
    state_acronym = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=15)
    # coordinate
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

class Cause(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True, null=False)
    description = models.text()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

class Organization_Causes(models.Model):
    id = models.AutoField(primary_key=True)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    cause_id = models.ForeignKey(Cause, on_delete=models.CASCADE)

class User_Organization_Role(models.Model):
    id = models.AutoField(primaryKey=True)
    name = models.CharField(max_length=50, unique=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


class Users_Organizations(models.Model):
    id = models.AutoField(primary_key=True)
    organization_id = models.ForeignKey(Organization)
    user_id = models.ForeignKey(User)
    role_id = models.ForeignKey(User_Organization_Role)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

class Donation_item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_quantity = models.IntegerField()
    open_quantity = models.IntegerField()


class Donation_type(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)


class Donation(models.Model):
    user_donation_request = models.IntegerField()
    description = models.TextField()
    donation_item = models.ForeignKey(Donation_item, on_delete=models.CASCADE)
    donation_user_id_request = models.IntegerField()
    donation_type_id = models.ForeignKey(Donation_type, on_delete=models.CASCADE)

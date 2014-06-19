from django.contrib.auth.models import User, Group
from rest_framework import serializers
from procedure.models import *

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        exclude = ('id', 'user')
        read_only_fields = ('id', 'create_date', 'update_date')

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Step

class PrecedenceSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Precedence
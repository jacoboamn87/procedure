
from procedure.models import *
from procedure.serializers import *
from rest_framework import status, generics, permissions, viewsets


class ProcedureViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProcedureSerializer
    queryset = Procedure.objects.all()


class StepViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StepSerializer
    queryset = Step.objects.all()


class PrecedenceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PrecedenceSerializer
    queryset = Precedence.objects.all()

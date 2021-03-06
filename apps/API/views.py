from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.permissions import IsAuthenticated
import P12_backend.permissions as perms
from .api_filters import *


class ApiViewsetMixin:
    """
    Mixin handling permissions and serializers selection for each viewset
    """
    serializer_actions = ['retrieve']
    edit_serializer = ['update', 'partial_update']

    read_actions = ['list', 'retrieve']
    edit_actions = ['update', 'partial_update']

    serializer_class = None
    create_serializer_class = None
    detail_serializer_class = None
    edit_serializer_class = None

    permission_classes = [IsAuthenticated]
    edit_permissions = [IsAuthenticated, perms.IsSaleReferee]
    create_permissions = [IsAuthenticated, perms.IsSales]
    delete_permissions = [IsAuthenticated, perms.IsManager]

    def get_serializer_class(self):
        """
        serializer selection logic
        :return: serializer object
        """
        if self.action in self.serializer_actions:
            return self.detail_serializer_class
        elif self.action in self.edit_serializer:
            return self.edit_serializer_class
        elif self.action == 'create':
            return self.create_serializer_class
        return super().get_serializer_class()

    def get_permissions(self):
        """
        permissions logic
        :return: set of booelans for each permissions in selected
        permissions_class
        """
        if self.action in self.edit_actions:
            self.permission_classes = self.edit_permissions
        elif self.action =='create':
            self.permission_classes = self.create_permissions
        elif self.action == 'destroy':
            self.permission_classes = self.delete_permissions
        return super().get_permissions()


class CustomersViewset(ApiViewsetMixin, ModelViewSet):
    """
    Viewset for customers
    """
    serializer_class = ListCustomersSerializer
    create_serializer_class = CreateCustomerSerializer
    detail_serializer_class = DetailCustomersSerializer
    edit_serializer_class = EditCustomersSerializer

    filterset_class = CustomerFilter

    def get_queryset(self):
        return Customer.objects.all()


class ContractViewset(ApiViewsetMixin, ModelViewSet):
    """
    Viewset for Contract
    """
    serializer_class = ListContractSerializer
    create_serializer_class = CreateContractSerializer
    detail_serializer_class = DetailContractSerializer
    edit_serializer_class = EditContractSerializer

    filterset_class = ContractFilter

    def get_queryset(self):
        return Contract.objects.all()


class EventViewset(ApiViewsetMixin, ModelViewSet):
    """
    Viewset for Events
    """
    serializer_class = ListEventSerializer
    create_serializer_class = CreateEventSerializer
    detail_serializer_class = DetailEventSerializer
    edit_serializer_class = EditEventSerializer

    edit_permissions = [IsAuthenticated, perms.IsSupportReferee]
    create_permissions = [IsAuthenticated, perms.IsSales]

    filterset_class = EventFilter

    def get_queryset(self):
        return Event.objects.all()

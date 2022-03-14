from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.validators import UniqueTogetherValidator
from apps.API.models import Customer, Contract, Event
from apps.authenticate.serializers import EmbedCustomUserSerializer, \
    DetailCustomUserSerializer


class ContractMixin:
    def get_contract(self, instance):
        sale = instance.contract
        serializer = EmbedContractSerializer(sale)
        return serializer.data


class SaleMixin:
    def get_sale_contact(self, instance):
        sale = instance.sale_contact
        serializer = EmbedCustomUserSerializer(sale)
        return serializer.data


class CustomerMixin:
    def get_customer(self, instance):
        customer = instance.customer
        serializer = EmbeddedCustomerSerializer(customer)
        return serializer.data


class CreateCustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'mobile',
            'email',
            'company',
            'date_created',
            'date_updated',
            'sale_contact'

        )

        validators = [
            UniqueTogetherValidator(queryset=Customer.objects.all(),
                                    fields=['email'],
                                    message='email already associated with '
                                            'an existing customer'
                                    )
        ]

    def create(self, validated_data):
        if not 'mobile' in validated_data:
            validated_data['mobile'] = None
        user = self.context['request'].user
        validated_data['sale_contact'] = user
        return Customer.objects.create(**validated_data)


class ListCustomersSerializer(SaleMixin, ModelSerializer):
    sale_contact = SerializerMethodField()

    class Meta:
        model = Customer
        fields = (
            'id', 'company', 'first_name', 'last_name', 'sale_contact',
            'existing')


class DetailCustomersSerializer(SaleMixin, ModelSerializer):
    sale_contact = SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'


class EditCustomersSerializer(SaleMixin, ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class EmbeddedCustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'company', ]


class CreateContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'customer', 'amount', 'payement_due', 'sale_contact')



class ListContractSerializer(SaleMixin, ModelSerializer,
                             CustomerMixin):
    sale_contact = SerializerMethodField()
    customer = SerializerMethodField()

    class Meta:
        model = Contract
        fields = (
            'id', 'customer', 'status', 'amount', 'sale_contact')


class DetailContractSerializer(SaleMixin, ModelSerializer, CustomerMixin):
    sale_contact = SerializerMethodField()
    customer = SerializerMethodField()
    event = SerializerMethodField()

    class Meta:
        model = Contract
        fields = ('id', 'sale_contact', 'customer', 'date_created',
                  'event_created', 'date_updated', 'status', 'amount',
                  'payement_due', 'event')

    #
    def get_event(self, instance):
        try:
            event = Event.objects.get(contract_id=instance.id)
            serializer = EmbedEventSerializer(event)
            return serializer.data
        except:
            return None


class EmbedContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id']


class EditContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class CreateEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
        'id', 'customer', 'support_contact', 'event_status', 'attendees',
        'event_date', 'note', 'contract')


class ListEventSerializer(ModelSerializer, CustomerMixin):
    support_contact = SerializerMethodField()
    customer = SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id', 'customer', 'note', 'support_contact', 'event_date',
            'attendees')

    def get_support_contact(self, instance):
        support = instance.support_contact
        serializer = EmbedCustomUserSerializer(support)
        return serializer.data


class DetailEventSerializer(ModelSerializer, CustomerMixin, ContractMixin):
    support_contact = SerializerMethodField()
    customer = SerializerMethodField()
    contract = SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_support_contact(self, instance):
        support = instance.support_contact
        serializer = DetailCustomUserSerializer(support)
        return serializer.data


class EmbedEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id']


class EditEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
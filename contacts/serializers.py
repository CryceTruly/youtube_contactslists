from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ['country_code', 'phone_number', 'first_name',
                  'last_name', "picture_url", "is_favorite"]

from rest_framework import serializers
from api.models import ContactForm

class SerializersContactForm(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"


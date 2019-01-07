from contact.models import Contact
from rest_framework import serializers

from user.models import Account


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
    # account = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'

    def new(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Contact.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance

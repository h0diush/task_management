from rest_framework import serializers


class ExtendedModelSerializerMixin(serializers.ModelSerializer):
    class Meta:
        abstract = True

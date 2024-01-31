from rest_framework import serializers

from groups.models import Employee


class EmployeeShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id',)
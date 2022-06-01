from rest_framework import serializers
from BetweenTheoryAndPracticeEX2App.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'address', 'city', 'zip_code',
                  'landline', 'cellular_phone', 'is_covid_19_infected', 'have_diabetes',
                  'have_cardio_problems', 'have_allergies', 'have_other_medical_conditions')

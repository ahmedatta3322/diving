from rest_framework import serializers
from divers.models import Divers
class DiverSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Divers
        fields = '__all__'
 #   def validate_name(self , value):
  #      q = Divers.objects.filter(name__iexact = value)
   #     if q.exists():
    #        raise serializers.ValidationError("name wrong")
     #   return value

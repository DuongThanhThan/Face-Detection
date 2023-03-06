from rest_framework import serializers
from .models import Face_Detection, Time

class Face_Serializers(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required = True)
    full_name = serializers.CharField(required = True)
    email = serializers.CharField(max_length = 150, allow_blank = True, allow_null = True)
    image = serializers.CharField(max_length = 150, allow_blank = True, allow_null = True)
    created_time = serializers.CharField(max_length = 150, allow_blank = True, allow_null = True)

    class Meta:
        model = Face_Detection
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'write_only': True}
        }
    
    
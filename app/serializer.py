from rest_framework import serializers

from .models import PicturesModel


class PictureSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256, required=True, error_messages={"required": "Title is required field"})    
    type = serializers.CharField(max_length=256, required=True, error_messages={"required": "Type is required field"}) 
    position = serializers.IntegerField(required=False)
    image = serializers.FileField(required=True, error_messages={"required": "Image is required field"})


    class Meta:
        model = PicturesModel
        fields = "__all__"
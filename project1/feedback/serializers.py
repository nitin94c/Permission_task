from rest_framework import serializers
from .models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner = serializers.SerializerMethodField()

    class Meta:
        model = FeedBack
        fields = "__all__"
    
    def get_owner(self,obj):
        return obj.created_by.username
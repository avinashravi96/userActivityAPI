from .models import User, Activity
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):  
    start_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")
    end_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")
    class Meta:
        model = Activity
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','real_name', 'tz', 'activity_periods']

# MemberSerializer helps to get all fields data including activity periods 
class MemberSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many=True)
    class Meta:
        model = User
        fields = ['id','real_name', 'tz', 'activity_periods']



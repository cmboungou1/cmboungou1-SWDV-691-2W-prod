from rest_framework import serializers
from base.models import Goal

class GoalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Goal
		fields ='__all__'

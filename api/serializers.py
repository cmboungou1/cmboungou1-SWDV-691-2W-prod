from rest_framework import serializers
from base.models import Goal, Gpa, Sat

class SatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sat
		read_only_fields = ("id",)
		fields ='__all__'

class GpaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gpa
		read_only_fields = ("id",)
		fields ='__all__'

class GoalSerializer(serializers.ModelSerializer):  
    gpa = GpaSerializer(required=False)
    sat = SatSerializer(required=False)
    class Meta:
        model = Goal
        fields = ("id","user","title","description","type","category","completed","start_date","end_date","sat","gpa")
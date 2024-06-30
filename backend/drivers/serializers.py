from rest_framework import serializers
from .models.daily import Daily
from .models.work_period import WorkPeriod
from .models.driver import Driver

class DailySerializer(serializers.ModelSerializer):
	class Meta:
		model = Daily
		fields = '__all__'

class WorkPeriodSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkPeriod
		fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Driver
		fields = '__all__'
		
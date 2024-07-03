from rest_framework import serializers
from clients.serializers import ClientSerializer
from .models.daily import Daily
from .models.work_period import WorkPeriod
from .models.driver import Driver

class DailySerializer(serializers.ModelSerializer):
	class Meta:
		model = Daily
		fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
	client = ClientSerializer()
	
	class Meta:
		model = Driver
		fields = '__all__'
		
class WorkPeriodSerializer(serializers.ModelSerializer):
	driver = DriverSerializer()

	class Meta:
		model = WorkPeriod
		fields = '__all__'
		
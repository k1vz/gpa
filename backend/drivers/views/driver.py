from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from drivers.models.daily import Daily
from drivers.models.driver import Driver
from drivers.serializers import DriverSerializer, WorkPeriodSerializer, DailySerializer
from drivers.models.work_period import WorkPeriod

class DriverCreateView(APIView):
	# permission_classes = [IsAuthenticated]

	def post(self, req):
		serializer = DriverSerializer(data=req.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

class DriverDetailView(generics.RetrieveAPIView):
	# permission_classes = [IsAuthenticated]

	def get(self, req, pk):
		try:
			driver = Driver.objects.get(pk=pk)
		except Driver.DoesNotExist:
			return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

		work_periods = WorkPeriod.objects.filter(driver=driver)
		work_periods_data = []

		for work_period in work_periods:
			dailies = Daily.objects.filter(work_period=work_period)
			work_period_data = WorkPeriodSerializer(work_period).data
			work_period_data['dailies'] = DailySerializer(dailies, many=True).data
			work_periods_data.append(work_period_data)

		response_data = {
			'driver': DriverSerializer(driver).data,
			'work_periods': work_periods_data
		}

		return Response(response_data, status=status.HTTP_200_OK)

class DriverListView(APIView):
	# permission_classes = [IsAuthenticated]

	def get(self, req):
		drivers = Driver.objects.all()
		drivers_data = []

		for driver in drivers:
			work_periods = WorkPeriod.objects.filter(driver=driver)
			work_periods_data = []

			for work_period in work_periods:
				dailies = Daily.objects.filter(work_period=work_period)
				work_period_data = WorkPeriodSerializer(work_period).data
				work_period_data['dailies'] = DailySerializer(dailies, many=True).data
				work_periods_data.append(work_period_data)

			driver_data = DriverSerializer(driver).data
			driver_data['work_periods'] = work_periods_data
			drivers_data.append(driver_data)

		return Response(drivers_data, status=status.HTTP_200_OK)


class DriverUpdateView(APIView):
	# permission_classes = [IsAuthenticated]

	def put(self, req, pk):
		try:
			driver = Driver.objects.get(pk=pk)
		except Driver.DoesNotExist:
			raise NotFound('Driver not found')

		serializer = DriverSerializer(driver, data=req.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverDeleteView(APIView):
	# permission_classes = [IsAuthenticated]

	def delete(self, req, pk):
		try:
			driver = Driver.objects.get(pk=pk)
		except Driver.DoesNotExist:
			raise NotFound('Driver not found')

		driver.active = False
		driver.save()

		return Response({'message': 'Driver deactivated successfully'}, status=status.HTTP_204_NO_CONTENT)
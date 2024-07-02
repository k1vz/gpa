from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from drivers.models.work_period import WorkPeriod
from drivers.serializers import WorkPeriodSerializer

class WorkPeriodCreateView(APIView):
	def post(self, req):
		serializer = WorkPeriodSerializer(data=req.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

class WorkPeriodDetailView(APIView):
	def get(self, req, pk):
		try:
			work_period = WorkPeriod.objects.get(pk=pk)
		except WorkPeriod.DoesNotExist:
			raise NotFound('Work Period not found')

		serializer = WorkPeriodSerializer(work_period)

		return Response(serializer.data)

class WorkPeriodListView(APIView):
	def get(self, req):
		work_periods = WorkPeriod.objects.all()
		serializer = WorkPeriodSerializer(work_periods, many=True)

		return Response(serializer.data)

class WorkPeriodUpdateView(APIView):
	def put(self, req, pk):
		try:
			work_period = WorkPeriod.objects.get(pk=pk)
		except WorkPeriod.DoesNotExist:
			raise NotFound('Work Period not found')

		serializer = WorkPeriodSerializer(work_period, data=req.data)
		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkPeriodDeleteView(APIView):
	def delete(self, req, pk):
		try:
			work_period = WorkPeriod.objects.get(pk=pk)
		except WorkPeriod.DoesNotExist:
			raise NotFound('Work Period not found')

		work_period.delete()

		return Response({'message': 'Work Period deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
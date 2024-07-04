from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from drivers.models.daily import Daily
from drivers.serializers import DailySerializer

class DailyCreateView(APIView):
    def post(self, req):
        serializer = DailySerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
		
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DailyDetailView(APIView):
	def get(self, req, pk):
		try:
			daily = Daily.objects.get(pk=pk)
		except Daily.DoesNotExist:
			raise NotFound('Daily record not found')

		serializer = DailySerializer(daily)

		return Response(serializer.data)

class DailyListView(APIView):
	def get(self, req):
		dailies = Daily.objects.all()
		serializer = DailySerializer(dailies, many=True)

		return Response(serializer.data)

class DailyUpdateView(APIView):
	def put(self, req, pk):
		try:
			daily = Daily.objects.get(pk=pk)
		except Daily.DoesNotExist:
			raise NotFound('Daily record not found')

		serializer = DailySerializer(daily, data=req.data)
		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DailyDeleteView(APIView):
	def get(self, req, pk):
		try:
			daily = Daily.objects.get(pk=pk)
		except Daily.DoesNotExist:
			raise NotFound('Daily record not found')

		daily.delete()

		return Response({'message': 'Daily record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
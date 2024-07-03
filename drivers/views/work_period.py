from django.shortcuts import redirect, render
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from drivers.forms import WorkPeriodForm
from drivers.models.work_period import WorkPeriod
from drivers.serializers import WorkPeriodSerializer

class WorkPeriodCreateView(View):
	def get(self, req):
		work_period_form = WorkPeriodForm()

		return render(req, 'cadastrar_jornada.html', {
			'form': work_period_form,
		})
	
	def post(self, req):
		work_period_form = WorkPeriodForm(req.POST)

		if work_period_form.is_valid():
			work_period = work_period_form.save(commit=False)

			work_period.save()
		else:
			print(work_period_form.errors)

		return redirect('work-period-list')
	
class WorkPeriodListView(APIView):
	def get(self, req):
		work_periods = WorkPeriod.objects.all()
		serializer = WorkPeriodSerializer(work_periods, many=True)

		return render(req, 'jornadas.html', {'work_periods': serializer.data})

class WorkPeriodCreateAPIView(APIView):
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

class WorkPeriodListAPIView(APIView):
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
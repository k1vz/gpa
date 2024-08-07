from django.urls import reverse
from django.views import View
from rest_framework import status
from rest_framework import generics
from drivers.forms import DriverForm, WorkPeriodForm
from drivers.models.daily import Daily
from rest_framework.views import APIView
from drivers.models.driver import Driver
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.exceptions import NotFound
from drivers.models.work_period import WorkPeriod
from drivers.serializers import DriverSerializer, WorkPeriodSerializer, DailySerializer

class DriverCreateView(View):
	def get(self, req):
		driver_form = DriverForm()

		return render(req, 'create/create_driver.html', {
			'form': driver_form,
		})

	def post(self, req):
		driver_form = DriverForm(req.POST)

		if driver_form.is_valid():
			driver = driver_form.save(commit=False)

			driver.save()
		else:
			print(driver_form.errors)

		return redirect('driver-list')

class DriverDetailView(generics.RetrieveAPIView):
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

		driver_data = DriverSerializer(driver).data

		return render(req, 'detail/detail_driver.html', {'driver': driver_data, 'work_periods': work_periods_data})

class DriverListView(APIView):
	def get(self, req):
		drivers = Driver.objects.all()
		serializer = DriverSerializer(drivers, many=True)

		return render(req, 'view/view_drivers.html', {'drivers': serializer.data})

class DriverUpdateView(View):
	def get(self, req, pk):
		driver = get_object_or_404(Driver, pk=pk)
		driver_form = DriverForm(instance=driver)
		
		return render(req, 'update/update_driver.html', {
			'driver_form': driver_form,
			'driver': driver
		})

	def post(self, req, pk):
		driver = get_object_or_404(Driver, pk=pk)
		driver_form = DriverForm(req.POST, instance=driver)

		if driver_form.is_valid():
			driver_form.save()
			return redirect('driver-detail', pk=pk)
		else:
			return render(req, 'update/update_driver.html', {
				'form': driver_form,
				'driver': driver
			})

class DriverDeleteView(APIView):
	def get(self, req, pk):
		try:
			driver = Driver.objects.get(pk=pk)
		except Driver.DoesNotExist:
			raise NotFound('Driver not found')

		driver.delete()

		return redirect(reverse('driver-list'))

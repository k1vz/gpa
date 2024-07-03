from django import forms
from .models.driver import Driver
from .models.work_period import WorkPeriod

class DriverForm(forms.ModelForm):
	birth_date = forms.DateField(
		label='Data de Nascimento',
		widget=forms.DateInput(attrs={'type': 'date'})
	)
	
	class Meta:
		model = Driver
		fields = '__all__'
		labels = {
			'name': 'Nome',
			'cpf': 'CPF',
			'birth_date': 'Data de Nascimento',
			'license_type': 'Tipo da CNH',
			'cnh': 'CNH',
			'demerit_points': 'Pontos na CNH',
			'client': 'Cliente Associado'
		}
		widgets = {
			'license_type': forms.Select(choices=Driver.LICENSE_TYPE)
		}

class WorkPeriodForm(forms.ModelForm):
	class Meta:
		model = WorkPeriod
		fields = ['responsibleSignature', 'periodStart', 'periodEnd', 'driver']
		labels = {
			'responsibleSignature': 'Assinatura Responsável',
			'periodStart': 'Início do Período',
			'periodEnd': 'Fim do Período',
			'driver': 'Motorista'
		}
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['periodStart'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
		self.fields['periodEnd'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
		self.fields['driver'].queryset = Driver.objects.all()

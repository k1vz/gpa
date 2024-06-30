from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models.driver import Driver
from django.contrib.auth.models import User

class DriverTests(APITestCase):
    
    def setUp(self):
        # Create a sample user and driver for testing purposes
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.driver = Driver.objects.create(
            name="Test Driver",
            cpf="12345678901234",
            birthDate="1990-01-01",
            licenseType="B",
            cnh="12345678901",
            licensePoints=0,
            active=True,
            fk_Client_idClient=1
        )
        
        # URL endpoints
        self.driver_list_url = reverse('driver-list')
        self.driver_detail_url = reverse('driver-detail', kwargs={'pk': self.driver.id})
        self.driver_register_url = reverse('driver-register')
        self.driver_update_url = reverse('driver-update', kwargs={'pk': self.driver.id})
        self.driver_delete_url = reverse('driver-delete', kwargs={'pk': self.driver.id})

    def test_driver_list(self):
        response = self.client.get(self.driver_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_driver_register(self):
        data = {
            "name": "New Driver",
            "cpf": "09876543210987",
            "birthDate": "1985-05-05",
            "licenseType": "A",
            "cnh": "09876543210",
            "licensePoints": 5,
            "active": True,
            "fk_Client_idClient": 2
        }
        response = self.client.post(self.driver_register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_driver_detail(self):
        response = self.client.get(self.driver_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_driver_update(self):
        data = {
            "name": "Updated Driver",
            "cpf": "12345678901234",
            "birthDate": "1990-01-01",
            "licenseType": "B",
            "cnh": "12345678901",
            "licensePoints": 10,
            "active": False,
            "fk_Client_idClient": 1
        }
        response = self.client.put(self.driver_update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_driver_delete(self):
        response = self.client.delete(self.driver_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

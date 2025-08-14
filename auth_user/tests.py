from django.test import TestCase
from .models import *

# Create your tests here.

class AnimalTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username = "emailTest1@gmail.com",
            name="Usuário Teste 1",
            email="emailTest1@gmail.com",
            cpf="00000000000"
        )
        User.objects.create(
            username = "emailTest2@gmail.com",
            name="Usuário Teste 2",
            email="emailTest2@gmail.com",
            cpf="00000000001"
        )

    def test_animals_can_speak(self):
        user1 = User.objects.get(cpf="00000000000")
        user2 = User.objects.get(cpf="00000000001")
        self.assertEqual(user1.name, 'Usuário Teste 1')
        self.assertEqual(user2.name, 'Usuário Teste 2')
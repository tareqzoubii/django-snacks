from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class snackTests(SimpleTestCase):
     def test_homePageStatus(self):
          url = reverse('home')
          responce = self.client.get(url)
          self.assertEqual(responce.status_code, 200)
     
     def test_aboutPageStatus(self):
          url = reverse('about')
          responce = self.client.get(url)
          self.assertEqual(responce.status_code, 200)
     
     def test_homePageTemplate(self):
          url = reverse('home')
          responce = self.client.get(url)
          print(responce)
          self.assertTemplateUsed(responce, 'home.html')
     
     def test_aboutPageTemplate(self):
          url = reverse('about')
          responce = self.client.get(url)
          self.assertTemplateUsed(responce, 'about.html')
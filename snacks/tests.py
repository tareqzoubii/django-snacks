from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class snackTests(SimpleTestCase):
     def homePageStatus(self):
          url = reverse('home')
          responce = self.client.get(url)
          self.assertEqual(responce.status_code, 200)
     def aboutPageStatus(self):
          url = reverse('about')
          responce = self.client.get(url)
          self.assertEqual(responce.status_code, 200)
     def homePageTemplate(self):
          url = reverse('home')
          responce = self.client.get(url)
          self.assertTemplateUsed(responce, 'home')
     def aboutPageTemplate(self):
          url = reverse('home')
          responce = self.client.get(url)
          self.assertTemplateUsed(responce, 'about')
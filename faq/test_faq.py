from django.test import TestCase
from .models import FAQ

class FAQTests(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="A Python web framework.")
        self.assertEqual(faq.get_translation('hi'), "Django क्या है?")

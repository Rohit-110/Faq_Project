from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer

from django.core.cache import cache

@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')
    cache_key = f"faqs_{lang}"
    data = cache.get(cache_key)

    if not data:
        faqs = FAQ.objects.all()
        data = [{'question': faq.get_translation(lang), 'answer': faq.answer} for faq in faqs]
        cache.set(cache_key, data, timeout=3600)

    return Response(data)

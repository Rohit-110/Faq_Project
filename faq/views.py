from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer
from googletrans import Translator


@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    data = [{'question': faq.get_translation(lang), 'answer': faq.answer} for faq in faqs]
    return Response(data)

@api_view(['GET'])
def get_faq(request, id):
    try:
        faq = FAQ.objects.get(id=id)
        lang = request.GET.get('lang', 'en')
        data = {'question': faq.get_translation(lang), 'answer': faq.answer}
        return Response(data)
    except FAQ.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_faq(request):
    if request.method == 'POST':
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            faq = serializer.save()
            return Response(FAQSerializer(faq).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_faq(request, id):
    try:
        faq = FAQ.objects.get(id=id)
    except FAQ.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FAQSerializer(faq, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_faq(request, id):
    try:
        faq = FAQ.objects.get(id=id)
    except FAQ.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    faq.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

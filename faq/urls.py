from django.urls import path
from . import views

urlpatterns = [
    path('faqs/', views.get_faqs, name='get_faqs'),
    path('faqs/<int:id>/', views.get_faq, name='get_faq'), 
    path('faqs/create/', views.create_faq, name='create_faq'),  
    path('faqs/<int:id>/update/', views.update_faq, name='update_faq'), 
    path('faqs/<int:id>/delete/', views.delete_faq, name='delete_faq'),  
]

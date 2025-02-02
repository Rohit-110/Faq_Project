from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    
    def get_translation(self, lang):
        return getattr(self, f'question_{lang}', self.question)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        super().save(*args, **kwargs)


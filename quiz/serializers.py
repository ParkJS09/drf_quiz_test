# 모델을 Json 형식으로 만들어주는 serializers.py를 통해 처리.

from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Quiz
        fields = ('title', 'body', 'answer')
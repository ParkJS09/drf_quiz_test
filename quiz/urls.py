#해당 프로젝트 내의 url을 맵핑

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Quiz
# from .serializers import QuizSerializer
#
# @api_view(['GET'])
# def helloAPI(request):
#     return Response("Hello World")

from django.urls import path
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]
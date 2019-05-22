from django.http import HttpResponse
from django.template import loader

from .models import Question

from rest_framework import generics
from rest_framework import mixins

from .serializers import QuestionSerializer

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))
    # leave the rest of the views (detail,results ,vote)unchanged


class pollsAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    resource_name = 'polls'
    serializer_class = QuestionSerializer

    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()

        def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)

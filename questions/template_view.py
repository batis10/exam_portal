from django.views.generic import ListView

from .models import Question  # Import your Question model here



class QuestionListView(ListView):
    model = Question # Replace with your actual model name
    template_name = 'questions.html'  # Replace with your actual template path
    context_object_name = 'questions'  # The name of the variable to be used in the template


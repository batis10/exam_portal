from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render
from django.views import View
from .models import Question  # Import your Question model here

# List view for questions, requires login
class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'questions.html'  # Replace with your actual template path
    context_object_name = 'questions'  # The name of the variable to be used in the template
    login_url = '/login/'  # Redirect to login page if not logged in
    redirect_field_name = 'redirect_to'  # Redirect back to the original page after login

# Example view with LoginRequiredMixin to ensure the user is logged in
class MyView(LoginRequiredMixin, View):
    login_url = '/login/'  # Redirect to login if not logged in
    redirect_field_name = 'redirect_to'  # Custom redirect field name
    
    def get(self, request, *args, **kwargs):
        return render(request, 'my_template.html')  # Replace with your actual template

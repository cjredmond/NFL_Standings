from django.shortcuts import render
from django.views.generic import ListView
from nfl.models import Team

class IndexView(ListView):
    model = Team

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     return context

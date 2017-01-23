from django.shortcuts import render
from django.views.generic import ListView
from nfl.models import Team

class IndexView(ListView):
    model = Team

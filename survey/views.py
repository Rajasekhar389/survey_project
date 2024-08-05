from django.shortcuts import render, redirect
from .models import Question, Option, Response
from .forms import SurveyForm
from collections import defaultdict
import matplotlib.pyplot as plt
import io
import urllib, base64

from django.shortcuts import render

def survey_view(request):
    return render(request, 'survey/survey.html')

def results_view(request):
    return render(request, 'survey/results.html')  # Assuming you have a results.html


import os
from django.conf import settings

def survey_view(request):
    template_dirs = settings.TEMPLATES[0]['DIRS']
    app_dirs = settings.TEMPLATES[0]['APP_DIRS']
    print(f"Template Dirs: {template_dirs}")
    print(f"App Dirs: {app_dirs}")
    return render(request, 'survey/survey.html')

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
    responses = Response.objects.all()
    trait_counts = defaultdict(int)
    traits = {
        "Neuroticism": ["Very Accurate", "Moderately Accurate"],
        "Extraversion": ["Very Accurate"],
        "Openness to Experience": ["Very Accurate", "Moderately Accurate", "Neither Accurate Nor Inaccurate"],
        "Agreeableness": ["Very Inaccurate", "Moderately Inaccurate"],
        "Conscientiousness": ["Moderately Inaccurate", "Very Inaccurate", "Neither Accurate Nor Inaccurate"]
    }

    for response in responses:
        for trait, relevant_responses in traits.items():
            if response.option.text in relevant_responses:
                trait_counts[trait] += 1

    labels = list(trait_counts.keys())
    counts = list(trait_counts.values())
    colors = ['purple', 'blue', 'pink', 'yellow', 'green']

    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts, color=colors)
    plt.xlabel('Personality Traits')
    plt.ylabel('Count')
    plt.title('Survey Responses by Personality Traits')
    plt.xticks(rotation=45)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return render(request, 'survey/results.html', {'data': uri})

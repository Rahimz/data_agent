from django.shortcuts import render
from .forms import QuestionForm
import requests


"""
while true; do cat response.http | nc -l -p 8888; done
"""

def HomeView(request):
    response_data = ''
    if request.method == 'POST':
        form= QuestionForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            question = cd['question']
            url = 'http://127.0.0.1:8888/ask'
            headers = {
                "Content-Type": "application/json"
            }
            payload = {
                "question": question
            }
            response = requests.post(url, headers=headers, json=payload) # Use json=payload for automatic JSON encoding

            response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

            response_data = response.json()
            # i want to show the response
    else:
        form = QuestionForm()
        
    context = dict(
        form=form,
        response_data=response_data
    )
    return render(
        request, 
        'home.html',
        context
    )        

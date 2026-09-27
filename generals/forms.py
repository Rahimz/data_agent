from django import forms 


class QuestionForm(forms.Form):
    question = forms.CharField(
        label='Question',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your question here'})
    )

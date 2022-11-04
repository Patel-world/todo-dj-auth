from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']

class PositionForm(forms.Form):
    position = forms.CharField()  

class CompletedForm(forms.Form)      :
    complete = forms.CharField()
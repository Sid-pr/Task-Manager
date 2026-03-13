from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'due_date',
            'status',
            'remarks',
            'created_by',
            'updated_by'
        ]
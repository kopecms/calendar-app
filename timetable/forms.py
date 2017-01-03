from django import forms
from timetable.models import Task

EMPTY_ITEM_ERROR = "You can't have an empty list item"

class TaskForm(forms.models.ModelForm):

    class Meta:
        model = Task
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'id':'post-text',
                'placeholder': 'Enter task to-do',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }

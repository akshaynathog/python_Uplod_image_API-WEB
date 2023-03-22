from django import forms
from stack.models import Questions

class QuestionForm(forms.ModelForm):

    class Meta:
        model=Questions
        fields=[
            "question",
            "image",
        ]
        widgets={
            "question":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "image":forms.FileInput(attrs={"class":"form-select"})
        }
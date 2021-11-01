from django.forms import ModelForm, fields
from .models import Library, Student
class AddBookForm(ModelForm):
    class Meta:
        model=Library
        fields=['book','category','language','description','publisher','paperback','sid']
from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    # Custom validation for name
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")
        return name
    # Custom validation for age
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("Age must be 18 or above.")
        return age
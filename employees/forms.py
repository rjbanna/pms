from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 255)
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username and not password:
            raise forms.ValidationError('Add username and password')


class AddClient(forms.ModelForm):
    CHOICES=[
        (1,'Yes'),
        (0,'No')
    ]

    active = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Client
        fields = ('name', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'country', 'active')


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ('designation',)


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ('technology',)


class InterviewForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Interview
        fields = '__all__'

class KnowledgeForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea )

    class Meta:
        model = Knowledge
        fields = '__all__'

class PerformanceQuestionForm(forms.ModelForm):
    class Meta:
        model = PerformanceQuestion
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    description = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = Project
        fields = ('title', 'description', 'start_date', 'end_date', 'project_files')

class ProjectAssignForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title',)

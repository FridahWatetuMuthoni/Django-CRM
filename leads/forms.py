from . models import Lead, Agent, Category
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'age', 'agent']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {"username": UsernameField}


class AssignAgentForm(forms.Form):
    # agent = forms.ChoiceField() =>takes in choices
    # ModelChoiceField takes in a queryset
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())
    # dynamically specify the queryset
    # accesing the request object that was passed to the form in the views

    def __init__(self, *args, **kwargs):
        print(kwargs)
        # Removing the request object from the form context because the form will not be expecting it
        request = kwargs.pop('request')
        print(request.user)
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        # updating the queryset dynamically
        self.fields['agent'].queryset = agents


class LeadCategoryForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['category']

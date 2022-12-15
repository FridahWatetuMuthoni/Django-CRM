from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentForm
from .mixins import OrganiserAndLoginRequiredMixin
from django.core.mail import send_mail
import random


# Create your views here.


class AgentsListView(OrganiserAndLoginRequiredMixin, ListView):
    template_name = 'agents_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        print(organisation)
        return Agent.objects.filter(organisation=organisation)


class AgentsCreateView(OrganiserAndLoginRequiredMixin, CreateView):
    form_class = AgentForm
    template_name = 'agents_create.html'

    def get_success_url(self):
        return reverse('agents:agents_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        email = form.cleaned_data['email']
        user.is_agent = True
        user.is_organiser = False
        password = f'{random.randint(0,100000000)}'
        user.set_password(password)
        user.save()
        Agent.objects.create(
            user=user, organisation=self.request.user.userprofile)
        send_mail(
            subject='You are invited to be an agent',
            message=f'You were added as an agent on DJCRM.Please come login to start working,your username:{user.username},email: {user.email}, password:{password}',
            from_email='djcrm@gmail.com',
            recipient_list=[f'{email}']
        )
        return super(AgentsCreateView, self).form_valid(form)


class AgentDetailView(OrganiserAndLoginRequiredMixin, DetailView):
    context_object_name = 'agent'
    template_name = 'agents_detail.html'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse('agents:agents_list')


class AgentUpdateView(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = 'agents_update.html'
    form_class = AgentForm

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse('agents:agents_list')


class AgentDeleteView(OrganiserAndLoginRequiredMixin, DeleteView):
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse('agents:agents_list')



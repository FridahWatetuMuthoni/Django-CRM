from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.mail import send_mail
from .models import Lead, Agent, Category
from .forms import LeadForm, CustomUserCreationForm, AssignAgentForm, LeadCategoryForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganiserAndLoginRequiredMixin


# Create your views here.
class Signup_View(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class Home_Page_View(TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('leads:leads')
        return super(Home_Page_View, self).dispatch(request, *args, **kwargs)


""" 
def home_page(request):
    return render(request, 'home.html')
"""


class Leads_List_view(LoginRequiredMixin, ListView):
    template_name = 'leads_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            # filter to current logged in user
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Leads_List_view, self).get_context_data(**kwargs)
        if self.request.user.is_organiser:
            # checking is a foreigein key is null agent__isnull=True
            queryset = Lead.objects.filter(
                organisation=self.request.user.userprofile, agent__isnull=True)
            context.update({
                'unassigned_leads': queryset
            })
        return context


""" def leads_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads_list.html', context)
"""


class Leads_Detail_View(LoginRequiredMixin, DetailView):
    template_name = 'lead_detail.html'
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            # filter to current logged in user
            queryset = Lead.objects.filter(agent__user=user)
        return queryset


"""
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    print(pk)
    context = {
        'lead': lead
    }
    return render(request, 'lead_detail.html', context)
"""


class Leads_Create_View(LoginRequiredMixin, CreateView):
    template_name = 'lead_create.html'
    form_class = LeadForm

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        lead.save()
        # sends email
        send_mail(
            subject="The lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=[f'{self.request.user.email}']
        )
        return super(Leads_Create_View, self).form_valid(form)

    def get_success_url(self):
        return reverse('leads:leads')


"""
def create_lead(request):
    print(request.user)
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:leads')

    context = {
        'form': form
    }

    return render(request, 'lead_create.html', context)
"""


class Leads_Update_View(LoginRequiredMixin, UpdateView):
    template_name = 'lead_update.html'
    form_class = LeadForm
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            # filter to current logged in user
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

    def get_success_url(self):
        return reverse("leads:leads")


"""
def update_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(instance=lead)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:leads')

    context = {
        'form': form,
        "lead": lead
    }
    return render(request, 'lead_update.html', context)
"""


class Leads_Delete_View(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            # filter to current logged in user
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

    def get_success_url(self):
        return reverse("leads:leads")


"""def delete_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.delete()
    return redirect('leads:leads')
"""


class AssignAgentView(OrganiserAndLoginRequiredMixin, FormView):
    template_name = 'assign_agent.html'
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request': self.request
        })
        # passing request to the form
        return kwargs

    def get_success_url(self):
        return reverse('leads:leads')

    def form_valid(self, form):
        print(form.cleaned_data)
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)

        if self.request.user.is_organiser:
            queryset = Lead.objects.filter(
                organisation=self.request.user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=self.request.user.agent.organisation)

        context.update({
            'unassigned_lead_count': queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organiser:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(
                organisation=user.agent.organisation)

        return queryset


class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        # self.object gets the instance of the category that we are working with
        current_category = self.get_object()
        # The default is lead_set but since we added the related name we now use it
        queryset = current_category.leads.all()
        print(queryset)
        context.update({
            'leads': queryset
        })
        return context

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organiser:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(
                organisation=user.agent.organisation)

        return queryset


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'category_update.html'
    form_class = LeadCategoryForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
        return queryset

    def get_success_url(self):
        return reverse('leads:detail', kwargs={'pk': self.get_object().id})

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.mail import send_mail
from .models import Lead, Agent
from .forms import LeadForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.


class Home_Page_View(TemplateView):
    template_name = 'home.html'


""" 
def home_page(request):
    return render(request, 'home.html')
"""


class Leads_List_view(ListView):
    template_name = 'leads_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


""" def leads_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads_list.html', context)
"""


class Leads_Detail_View(DetailView):
    template_name = 'lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"


"""
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    print(pk)
    context = {
        'lead': lead
    }
    return render(request, 'lead_detail.html', context)
"""


class Leads_Create_View(CreateView):
    template_name = 'lead_create.html'
    form_class = LeadForm

    def form_valid(self, form):
        # sends email
        send_mail(
            subject="The lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=['recipient@gmail.com']
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


class Leads_Update_View(UpdateView):
    template_name = 'lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadForm
    context_object_name = 'lead'

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


class Leads_Delete_View(DeleteView):
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:leads")


"""def delete_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.delete()
    return redirect('leads:leads')
"""

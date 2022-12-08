from django.shortcuts import render, get_object_or_404, redirect
from .models import Lead, Agent
from .forms import LeadForm

# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def leads_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads_list.html', context)


def leads_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    print(pk)
    context = {
        'lead': lead
    }
    return render(request, 'lead_detail.html', context)


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
        "lead":lead
    }
    return render(request, 'lead_update.html', context)


def delete_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.delete()
    return redirect('leads:leads')

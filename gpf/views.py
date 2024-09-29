# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import GPFFormForm, NomineeForm
from .models import GPFForm, Nominee
from django.template.loader import get_template
from xhtml2pdf import pisa

# GPF Form View

def gpf_form_view(request):
    if request.method == 'POST':
        form = GPFFormForm(request.POST)
        if form.is_valid():
            gpf_instance = form.save()  # Save GPF details
            request.session['gpf_form_id'] = gpf_instance.id  # Store ID in session
            return redirect('add_nominee', gpf_form_id=gpf_instance.id)  # Redirect to nominee form
    else:
        form = GPFFormForm()
    return render(request, 'gpf_form.html', {'form': form})


# Nominee Form View

def add_nominee_view(request, gpf_form_id):
    gpf_form = get_object_or_404(GPFForm, id=gpf_form_id)

    if request.method == 'POST':
        form = NomineeForm(request.POST)
        if form.is_valid():
            nominee_instance = form.save(commit=False)
            nominee_instance.gpf_form = gpf_form  # Associate nominee with GPF form
            nominee_instance.save()
            if 'add_more' in request.POST:
                return redirect('add_nominee', gpf_form_id=gpf_form_id)  # Redirect to add more nominees
            else:
                return redirect('download_pdf', gpf_form_id=gpf_form_id)  # Generate PDF
    else:
        form = NomineeForm()

    return render(request, 'add_nominee.html', {'form': form, 'gpf_form': gpf_form})


# PDF Download View

def download_pdf_view(request, gpf_form_id):
    gpf_form = get_object_or_404(GPFForm, id=gpf_form_id)
    nominees = Nominee.objects.filter(gpf_form=gpf_form)

    template_path = 'gpf/pdf_template.html'
    
    context = {
        'subscriber_name': gpf_form.subscriber_name,
        'marital_status': gpf_form.marital_status,
        'nominees': nominees,
        'place': 'YourPlace',  # Replace with dynamic data if needed
        'date': 'CurrentDate',  # Replace with dynamic data if needed
        'subscriber_signature': 'SignaturePlaceholder',  # Replace with dynamic data if needed
    }

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="gpf_form_{gpf_form_id}.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse(f'Error generating PDF: {pisa_status.err}', status=400)
    
    return response


from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from xhtml2pdf import pisa
from generator.models import Certificate

def generate_certificate_pdf(request):
    certificate = Certificate.objects.last()

    template_path = 'base/certificate_template.html'
    context = {
        'name': certificate.name,
        'course': certificate.course,
        'date': certificate.date,
    }

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{certificate.name}_certificate.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)

    return response

def create_certificate(request):
    if request.method == 'POST':
        name = request.POST['name']
        course = request.POST['course']
        date = request.POST['date']

        certificate = Certificate(name=name, course=course, date=date)
        certificate.save()

        return generate_certificate_pdf(request)
    else:
        return render(request, 'base/create_certificate.html')

from django.shortcuts import render

from job_application.forms import ApplicationForm
from job_application.models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            form_instance = Form(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)
            form_instance.save()

            subject = f"Form Submission Confirmation for {first_name} {last_name}"
            body = f"A new application has been submitted by {first_name} {last_name}."
            email_message = EmailMessage(subject, body, to=[email])
            email_message.send()



            messages.success(request, f"Thank you for your application, {first_name} {last_name}!")
    return render(request, 'index.html')
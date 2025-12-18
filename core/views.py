from django.shortcuts import render
from .forms import TestEmailForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone


# Homepage views
def index(request):
    form = TestEmailForm()
    if request.method == "POST":
        form = TestEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            name = form.cleaned_data["name"]
            text = render_to_string(
                "email/contact.txt",
                {
                    "site_name": "Django Localhost",
                    "name": name,
                    "email": email,
                    "message": message,
                    "date": timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
                },
            )
            send_mail(
                subject=subject,
                message=text,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )
    return render(request, "core/index.html", {"form": form})

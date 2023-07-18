from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'webpages/index.html')

def service(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')
def about(request):
    return render(request, 'webpages/aboutus.html')

from django.http import JsonResponse

def contact_submission(request):
    if request.method == "POST":
        name = request.POST.get('name')
        service = request.POST.get('service')
        messgae=request.POST.get('msg')
        phone=request.POST.get('phone')

        email = request.POST.get('email')
        print(f'name: {name}\nservice: {service}\nemail: {email} {messgae} {phone}')
        contact=Contact(name=name,service=service,email=email,message=messgae,phone=phone)
        contact.save()
        # Perform additional form processing or validation
        msg = f"""
            <html>
            <head>
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
                    body {{
                        font-family: 'Poppins', sans-serif;
                    }}
                </style>
            </head>
            <body>
                <h2>Contact Form Submission</h2>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Service:</strong> {service}</p>
                <p><strong>Message:</strong> {messgae}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>
            </body>
            </html>
        """
        # Return JSON response indicating success
        response_data = {'success': True, 'message': 'Form submitted successfully.'}
        send_email('developerfaddybro@gmail.com','Contact form',msg)

        return JsonResponse(response_data)
    # Return JSON response indicating failure
    response_data = {'success': False, 'message': 'Invalid request method.'}

    return JsonResponse(response_data)
from django.core.mail import EmailMessage

def send_email(receiver, subject, message):
    email = EmailMessage(
        subject=subject,
        body=message,
        to=[receiver],
        from_email='support@holywolfdesigns.com',  # Replace with your Gmail email address
    )
    email.content_subtype = 'html'
    email.send()

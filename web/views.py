from django.shortcuts import render
from .models import Contact,Analyticsdata,Realtimedata
#------------------for auth---------------------
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    getip(request)
    return render(request, 'webpages/index.html')

def service(request):
    getip(request)

    return render(request, 'webpages/services.html')

def contact(request):
    getip(request)

    return render(request, 'webpages/contact.html')
def about(request):
    getip(request)

    return render(request, 'webpages/aboutus.html')
from django.http import JsonResponse
from django.shortcuts import render
import time

from django.http import JsonResponse

def contact_submission(request):
    if request.method == "POST":
        name = request.POST.get('name')
        service = request.POST.get('service')
        messgae=request.POST.get('msg')
        phone=request.POST.get('phone')

        email = request.POST.get('email')
        #print(f'name: {name}\nservice: {service}\nemail: {email} {messgae} {phone}')
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

import requests,json
#----------------------Dashboard----------------------------#
api_key = 'a49d2329830f44fbbd78b7a689c4a73d'

api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key

@login_required
def dashboard(request):
    #getip(request)
    data = Analyticsdata.objects.all()

    # Create a list to hold the dictionaries
    analytics_list = []

    # Loop through the queryset and add each item as a dictionary to the list
    for item in data:
        #print(f'Time form data {item.time}')
        analytics_list.append({
            'ip_address': item.ip_address,
            'city': item.city,
            'region': item.region,
            'country': item.country,
            'time': item.time,  # Convert the datetime object to a string
            'total_view_count': item.total_view_count,
        })
    #print(json.dumps(analytics_list))
    # Create a JSON response with the data
    json_response = json.dumps(analytics_list)
    r1=realtime_views()
    json_realtime=json.dumps(list(r1.values()))
    json_realtime_all=json.dumps(list(Realtimedata.objects.all().values()))

    context={'json_data': json_response,
             'json_realtime': json_realtime,
             'json_realtime_all': json_realtime_all
             }
    # Render the HTML template and pass the JSON data as context
    
    return render(request, 'webpages/dashboard.html', context)
@login_required
def contactdetails(request):
    if request.user.is_superuser:
    # Create a list to hold the dictionaries
    # Loop through the queryset and add each item as a dictionary to the list
        json_contact_details=json.dumps(list(Contact.objects.all().values()))

        context={'json_contact': json_contact_details,
                
                }
        # Render the HTML template and pass the JSON data as context
        
        return render(request, 'webpages/contactdetails.html', context)
    else:
        messages.error(request, 'Only Admins Can Edit Data')
        return render(request, 'webpages/auth.html')
from datetime import datetime, timedelta
from django.db.models import Q
from django.core import serializers

def realtime_views_api(request):
    hour=request.GET.get('hour')
    print('Here are number of Hours ',request.GET.get('hour'))
    endtime=datetime.now()
    start_time = endtime - timedelta(hours=int(hour))
    print(start_time,endtime)
    realdata=Realtimedata.objects.filter(Q(time__range=(start_time, endtime)))
    data = serializers.serialize('json', realdata)
    # Return the JSON response
    return JsonResponse(list(realdata.values()), safe=False)
def realtime_views():
    endtime=datetime.now()
    start_time = endtime - timedelta(hours=int(24))
    realdata=Realtimedata.objects.filter(Q(time__range=(start_time, endtime)))
    #realdata_all=Realtimedata.objects.all()
    return realdata
#inseting responeded or not in db

def inserting_responded(request):
    respond_id = request.GET.get('id')
    Contact.objects.filter(id=respond_id).update(responded='yes')
    
    responded_row = Contact.objects.filter(id=respond_id).values()
    responded_row_list = list(responded_row)
    
    print(responded_row_list)
    
    return JsonResponse(responded_row_list, safe=False)
   
def get_ip_geolocation_data():

   # not using the incoming IP address for testing

   response = requests.get(api_url)

   return response.content



from django.shortcuts import render, HttpResponse



def user_details():

    geolocation_json = get_ip_geolocation_data()

    geolocation_data = json.loads(geolocation_json)
    city = geolocation_data['city']
    country = geolocation_data['country']
    ipadddress=geolocation_data['ip_address']
    region = geolocation_data['region']
    #print(f'Country {country}\nIp {ipadddress}')
    return ipadddress,city,region,country    

def getip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:

        ip = x_forwarded_for.split(',')[0]
    else:

        ip = request.META.get('REMOTE_ADDR')
    if isipindb(ip):
        #print(f'IP is in db')
        add_realtime_data(ip)
        update_view_count(ip)
    else:
        #print(f'is not in db')
        add_realtime_data(ip)
        add_datails(ip)
def add_realtime_data(ip):
    Realtimedata(ip_address=ip,time=time_zone(),total_view_count=1).save()
    return
def add_datails(ipaddress):
    ip,city,region,country=user_details()
    Analyticsdata(ip_address=ipaddress,city=city,country=country,region=region,total_view_count=1,time=time_zone()).save()
    return
import pytz
def time_zone():
    utc_time = datetime.now(pytz.utc)

    # Convert the UTC time to a specific time zone
    target_timezone = pytz.timezone('Asia/Karachi')
    local_time = utc_time.astimezone(target_timezone)

    return local_time
def update_view_count(user_ip):
    analytics_obj = Analyticsdata.objects.get(ip_address=user_ip)
    #Analyticsdata.objects.all().delete()
    # If the entry exists, update the total_view_count
    #print(f'Time Updated{(time_zone())}')
    analytics_obj.time=str(time_zone())
    analytics_obj.total_view_count += 1
    analytics_obj.save()
def isipindb(ip):
    try:
        Analyticsdata.objects.get(ip_address=ip)
        return True
    except:
        return False
    
#---------------------------------------------------Authentications



def auth(request):
    return render(request,'webpages/auth.html')
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email,email=email, password=password)
        print('Login successful')
        if user is not None:
            # User credentials are valid, log in the user
            login(request, user)
            print('Login successful')

            return HttpResponse(status=303, content='', headers={'Location': '/dashboard.html'})
        else:
            # User credentials are invalid, show an error message or handle the authentication failure
            return HttpResponse(status=404, content='', headers={'Location': '/auth.html'})

    return render(request, 'webpages/auth.html')
from django.urls import reverse

def register_view(request):
    if request.method == 'POST':
        print('register is working')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # Add your code to create a new user account with the provided email and password
            # For example, you can use Django's built-in User model to create the user:
            user = User.objects.create_user(username=email, email=email, password=password)

            # After creating the user, log them in
            login(request, user)
            print('register successful')

            return HttpResponse(status=303, content='', headers={'Location': '/dashboard.html'})
        else:
            # Passwords do not match, handle the error
            return render(request, 'webpages/auth.html', {'error': 'Passwords do not match.'})
        

    return HttpResponse(status=404, content='', headers={'Location': '/auth.html'})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return render(request, 'webpages/auth.html')
    #return render(request, 'register.html', {'form': form})
def login_vieww(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # If the user is already logged in, redirect them to the next page
        next_page = request.GET.get('next')
        if next_page:
            return redirect(next_page)
        else:
            return redirect('webpages/auth.html')  # Change 'dashboard' to the desired default page URL name

    # If the user is not logged in, handle the login logic here...
    # Your login logic here...

    return render(request, 'webpages/auth.html')
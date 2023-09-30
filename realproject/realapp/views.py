from django.shortcuts import render, redirect
from realapp.models import LandPlot, Car,House
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from math import ceil
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.db.models import Q


""" VIEWS """
""" home page arrangment """

def index(request):
    current_user = request.user
    print(current_user)
    allHouseAssets = []
    houseCats = House.objects.values('use', 'id')
    houseCatsSet = {item['use'] for item in houseCats}
    for cat in houseCatsSet:
        assets = House.objects.filter(use=cat)
        n = len(assets)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allHouseAssets.append([assets, range(1, nSlides), nSlides, range(nSlides)])  # Add range(nSlides) here

    allLandPlotAssets = []
    landPlotCats = LandPlot.objects.values('use', 'id')
    landPlotCatsSet = {item['use'] for item in landPlotCats}
    for cat in landPlotCatsSet:
        assets = LandPlot.objects.filter(use=cat)
        n = len(assets)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allLandPlotAssets.append([assets, range(1, nSlides), nSlides, range(nSlides)])  # Add range(nSlides) here

    allCarAssets = []
    carCats = Car.objects.values('use', 'id')
    carCatsSet = {item['use'] for item in carCats}
    for cat in carCatsSet:
        assets = Car.objects.filter(use=cat)
        n = len(assets)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allCarAssets.append([assets, range(1, nSlides), nSlides, range(nSlides)])  # Add range(nSlides) here

    params = {
        'houseAssets': allHouseAssets,
        'landPlotAssets': allLandPlotAssets,
        'carAssets': allCarAssets
    }
    return render(request, 'index.html', params)

""" PROPERTY SEARCH"""
def global_search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        house_results = House.objects.filter(
            Q(address__icontains=query) |  # Search by address
            Q(category__icontains=query) |  # Search by category
            Q(use__icontains=query)        # Search by use
        )

        car_results = Car.objects.filter(
            Q(carModel__icontains=query) |  # Search by car model
            Q(category__icontains=query) |  # Search by category
            Q(use__icontains=query)         # Search by use
        )

        landplot_results = LandPlot.objects.filter(
            Q(address__icontains=query) |  # Search by address
            Q(category__icontains=query) |  # Search by category
            Q(use__icontains=query)         # Search by use
        )

        results.extend(house_results)
        results.extend(car_results)
        results.extend(landplot_results)

    return render(request, 'global_search_results.html', {
        'query': query,
        'results': results,
    })
    

""" SENDING A MESSAGE """

def send_message(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Modify the message body to include sender's email
        message_body = f"From: {name}   <{email}>\n\n{message}"
        
        # Send email
        send_mail(
            'Hello Properties',  # subject of the email
            message_body,  # modified message body with sender's email
            email,  # sender's email
            ['hirwacedr12@gmail.com'],  # recipient's email
            fail_silently=False,
        )
        messages.success(request, 'Email sent successfully!')
        return redirect('index')  # Replace 'index' with the appropriate URL pattern name for your index page

    return render(request, 'index.html')



""" PROPERTY DETAILS"""
class HouseDetailView(DetailView):
    model = House
    template_name = 'property_detail.html'
class LandPlotDetailView(DetailView):
    model = LandPlot
    template_name = 'landplot_detail.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

def Signup(request):
    model = House
    return render (request,'signup.html')


  
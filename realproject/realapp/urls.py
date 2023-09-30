from django.urls import path
from realapp import views
from .views import send_message


urlpatterns = [
   path('',views.index, name='index'),


   path('send-message/index.html', send_message, name='send_message'),
   path('property_detail/<int:pk>/', views.HouseDetailView.as_view(), name='property_detail'),
   path('landplot_detail/<int:pk>/', views.LandPlotDetailView.as_view(), name='landplot_detail'),
   path('car_detail/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
   path('search/', views.global_search_view, name='global_search'),
   

   path('signup/', views.Signup, name='signup'),
]
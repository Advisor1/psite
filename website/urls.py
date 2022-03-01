from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
	path('about.html', views.about, name="about"),
	path('consultation.html', views.consultation, name="consultation"),
	path('contact.html', views.contact, name="contact"),
	path('general_insurance.html', views.general_insurance, name="general_insurance"),
	path('life.html', views.life, name="life"),
    path('partners.html', views.partners, name="partners"),
    path('sip.html', views.sip, name="sip"),
]

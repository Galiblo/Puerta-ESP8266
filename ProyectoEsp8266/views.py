from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests

ESP8266_IP = '192.168.1.33'  # Cambia por la dirección IP de tu ESP8266

@login_required
def control_led(request):
    return render(request, 'control_led.html')

def salir(request):
    logout(request)
    return redirect('/')

def encender_led(request):
    url = f"http://{ESP8266_IP}/encender"
    response = requests.get(url)
    if response.status_code == 200:
        return render(request, 'control_led.html')  # Otra vez a la página de control
    else:
        return HttpResponse("Error al encender el LED")

def apagar_led(request):
    url = f"http://{ESP8266_IP}/apagar"
    response = requests.get(url)
    if response.status_code == 200:
        return render(request, 'control_led.html')  # Otra vez a la página de control
    else:
        return HttpResponse("Error al apagar el LED")

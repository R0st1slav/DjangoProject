from django.shortcuts import render
from .models import Device, TypeDevice

def base(request):
    devices = Device.objects.all()
    return render(request, 'Notification/base.html', {'devices': devices})

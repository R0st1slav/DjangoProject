from django.shortcuts import render
from .models import Device, TypeDevice

def base(request):
    devices = Device.objects.all()
    type_devices = TypeDevice.objects.all()
    context = {
        'devices': devices,
        'type_devices': type_devices,
    }
    return render(request, 'base.html', context)

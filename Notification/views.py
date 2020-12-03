from django.shortcuts import render
from .models import Device, TypeDevice
from django.views.generic import ListView, TemplateView



# def devices(request):
#     devices = Device.objects.all()
#     context = {
#         'devices': devices,
#     }
#     return render(request, 'Notification/device.html', context)

class HomePageView(TemplateView):
    template_name = 'base.html'

    def render_to_response(self, context, **response_kwargs):
        devices = Device.objects.all()
        context = {
            'devices': devices,
        }
        # return self.response_class(request=request context=context)


class Search(ListView):
    model = Device
    template_name = 'Notification/filter_name.html'

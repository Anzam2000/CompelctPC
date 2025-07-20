from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PC


def home(request):
    return render(request, 'ComplectPCapp/index.html')


def submit_config(request):
    if request.method == 'POST':
        try:
            pc = PC(
                price=request.POST.get('price'),
                gpu=request.POST.get('GPU'),
                cpu=request.POST.get('CPU'),
                ram=request.POST.get('ram'),
                power_supply=request.POST.get('power_block'),
                memory=request.POST.get('memory'),
                cooler=request.POST.get('cooler'),
                case=request.POST.get('case'),
                motherboard=request.POST.get('motherboard'),

                gpu_market=request.POST.get('gpu_market'),
                cpu_market=request.POST.get('cpu_market'),
                ram_market=request.POST.get('ram_market'),
                power_supply_market=request.POST.get('power_supply_market'),
                memory_market=request.POST.get('memory_market'),
                cooler_market=request.POST.get('cooler_market'),
                case_market=request.POST.get('case_market'),
                motherboard_market=request.POST.get('motherboard_market')
            )
            pc.save()
            messages.success(request, 'Конфигурация успешно сохранена!')
            return redirect('ComplectPCapp:success_page')
        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')
            return redirect('ComplectPCapp:home')

    return redirect('ComplectPCapp:home')


def success_page(request):
    recent_configs = PC.objects.all().order_by('-id')[:1]
    return render(request, 'ComplectPCapp/success.html', {
        'configs': recent_configs
    })
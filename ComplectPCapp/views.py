import sqlite3

db_path = r"C:\Users\user\PycharmProjects\ComplectPC\ComplectPC\db.sqlite3"
#Получаем названия из базы
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Название FROM cpu LIMIT 1")
    cpu = cursor.fetchone()
    cpu = cpu[0]
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Название FROM gpu LIMIT 1")
    gpu = cursor.fetchone()
    gpu = gpu[0]
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Название FROM ram LIMIT 1")
    ram = cursor.fetchone()
    ram = ram[0]
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Название FROM cpu_cooler LIMIT 1")
    cooler = cursor.fetchone()
    cooler = cooler[0]
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Название FROM motherboard LIMIT 1")
    mb = cursor.fetchone()
    mb = mb[0]
#Получаем ссылки из базы
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Ссылка FROM cpu LIMIT 1")
    cpu_link = cursor.fetchone()
    cpu_link = cpu_link[0]
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Ссылка FROM gpu LIMIT 1")
    gpu_link = cursor.fetchone()
    gpu_link = gpu_link[0]
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Ссылка FROM ram LIMIT 1")
    ram_link = cursor.fetchone()
    ram_link = ram_link[0]
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Ссылка FROM cpu_cooler LIMIT 1")
    cooler_link = cursor.fetchone()
    cooler_link = cooler_link[0]
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Получаем только первую строку
    cursor.execute("SELECT Ссылка FROM motherboard LIMIT 1")
    mb_link = cursor.fetchone()
    mb_link = mb_link[0]
def home(request):
    return render(request, 'ComplectPCapp/index.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PC


def submit_config(request):
    if request.method == 'POST':
        try:
            # Магазины всегда из формы
            price = request.POST.get('price', '')
            gpu_market = request.POST.get('gpu_market', '')
            cpu_market = request.POST.get('cpu_market', '')
            ram_market = request.POST.get('ram_market', '')
            power_supply_market = request.POST.get('power_supply_market', '')
            memory_market = request.POST.get('memory_market', '')
            cooler_market = request.POST.get('cooler_market', '')
            case_market = request.POST.get('case_market', '')
            motherboard_market = request.POST.get('motherboard_market', '')

            # УБРАТЬ ЗАПЯТЫЕ после get() - они превращают значения в кортежи!
            gpu_form = request.POST.get('GPU', '')
            cpu_form = request.POST.get('CPU', '')
            ram_form = request.POST.get('ram', '')
            power_supply_form = request.POST.get('power_block', '')
            memory_form = request.POST.get('memory', '')
            cooler_form = request.POST.get('cooler', '')
            case_form = request.POST.get('case', '')
            motherboard_form = request.POST.get('motherboard', '')

            # Определяем, какие компоненты использовать
            use_gpu = gpu_form if gpu_form not in [None, ''] else gpu
            use_cpu = cpu_form if cpu_form not in [None, ''] else cpu
            use_ram = ram_form if ram_form not in [None, ''] else ram
            #use_power_supply = power_supply_form if power_supply_form not in [None, ''] else power_supply
            #use_memory = memory_form if memory_form not in [None, ''] else memory
            use_cooler = cooler_form if cooler_form not in [None, ''] else cooler
            #use_case = case_form if case_form not in [None, ''] else case
            use_motherboard = motherboard_form if motherboard_form not in [None, ''] else mb

            # Также получаем ссылки (предполагая, что переменные с ссылками тоже определены)
            use_gpu_link = '' if gpu_form not in [None, ''] else gpu_link
            use_cpu_link = '' if cpu_form not in [None, ''] else cpu_link
            use_ram_link = '' if ram_form not in [None, ''] else ram_link
            #use_power_supply_link = '' if power_supply_form not in [None, ''] else power_supply_link
            #use_memory_link = '' if memory_form not in [None, ''] else memory_link
            use_cooler_link = '' if cooler_form not in [None, ''] else cooler_link
            #use_case_link = '' if case_form not in [None, ''] else case_link
            use_motherboard_link = '' if motherboard_form not in [None, ''] else mb_link

            pc = PC(
                price=price,
                gpu=use_gpu,
                cpu=use_cpu,
                ram=use_ram,
                #power_supply=use_power_supply,  # Исправлено: было use_cooler
                #memory=use_memory,
                cooler=use_cooler,
                #case=use_case,
                motherboard=use_motherboard,

                # Добавляем ссылки
                gpu_link=use_gpu_link,
                cpu_link=use_cpu_link,
                ram_link=use_ram_link,
                #power_supply_link=use_power_supply_link,
                #memory_link=use_memory_link,
                cooler_link=use_cooler_link,
                #case_link=use_case_link,
                motherboard_link=use_motherboard_link,

                # Магазины из формы
                gpu_market=gpu_market,
                cpu_market=cpu_market,
                ram_market=ram_market,
                power_supply_market=power_supply_market,
                memory_market=memory_market,
                cooler_market=cooler_market,
                case_market=case_market,
                motherboard_market=motherboard_market
            )

            messages.success(request, 'Конфигурация успешно сохранена!')

            # Сохраняем
            pc.save()
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

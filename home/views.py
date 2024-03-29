import asyncio
from datetime import datetime

from django.shortcuts import render

from data_site.modelMasters import MastersModel
from data_site.modelPrice import PriceModel
from data_site.modelsDataSite import DataSiteModel
from home.formHome import FormHome
from home.save_statistic import save_click_from_statistic
from orders.models import OrderModel
from statistic.models import ClickersModule
from utils.get_ip import get_client_ip
from utils.logger._logger import logger_msg
from utils.logger.telegram.telegram_debug import Telegram
from utils.utils import change_number


def index(request):
    save_statistic = save_click_from_statistic(request)

    settings_sql = DataSiteModel.objects.first()

    price_list = PriceModel.objects.all()

    master_list = MastersModel.objects.all()

    try:
        context = {
            'brand_name': settings_sql.brand_name,
            'address': settings_sql.address,
            'tel': settings_sql.phone,
            'instagram': settings_sql.instagram,
            'title': settings_sql.title,
            'og_url': request.headers['host'],
            'description': settings_sql.description,
            'keywords': settings_sql.keywords,
            'og_description': settings_sql.og_description,
            'og_image': 'images/IMG_7259.PNG',
            'format_tel': change_number(settings_sql.phone),
            'form': FormHome(),
            'price_list': price_list,
            'masters': master_list,
            'year': datetime.now().year

        }
    except Exception as es:
        asyncio.run(logger_msg(f'Ошибка при формирования контекста "{es}"'))

        context = {}

    response = render(request, 'index.html', context=context)

    return response


def get_order(request):
    if request.method == "POST":
        form = FormHome(request.POST)

        if form.is_valid():

            ip = get_client_ip(request)

            name = form.cleaned_data['name']

            phone = form.cleaned_data['phone']

            url = request.POST.get('url', '-')

            order = OrderModel()

            order.name = name

            order.phone = phone

            order.ip = ip

            order.url = url

            try:
                order.id_client = request.COOKIES['sessionid']
            except:
                pass

            order.save()

            _msg = f'✅ Новая заявка {phone}%0A%0A' \
                   f'Имя: {name}%0A' \
                   f'Телефон: 📞<code>{phone}</code>'

            asyncio.run(Telegram().new_order(_msg))

            order_context = {
                'name': name,
                'phone': phone
            }

            response = render(request, 'thanks.html', context=order_context)

            return response

    return index(request)

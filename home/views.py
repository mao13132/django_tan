import asyncio

from django.shortcuts import render

from data_site.modelPrice import PriceModel
from data_site.modelsDataSite import DataSiteModel
from home.formHome import FormHome
from orders.models import OrderModel
from utils.logger.telegram.telegram_debug import Telegram
from utils.utils import change_number


# TODO проверить og


def index(request):
    settings_sql = DataSiteModel.objects.first()

    price_list = PriceModel.objects.all()

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

    }

    response = render(request, 'index.html', context=context)

    return response


def get_order(request):
    if request.method == "POST":
        form = FormHome(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            phone = form.cleaned_data['phone']

            order = OrderModel()

            order.name = name

            order.phone = phone

            try:
                order.id_client = request.COOKIES['sessionid']
            except:
                pass

            order.save()

            _msg = f'✅ Новая заявка {phone}%0A%0A' \
                   f'Имя: {name}%0A' \
                   f'Телефон: <code>{phone}</code>'

            asyncio.run(Telegram().new_order(_msg))

            order_context = {
                'name': name,
                'phone': phone
            }

            response = render(request, 'thanks.html', context=order_context)

            return response

    return index(request)

import asyncio

from django.shortcuts import render

from data_site.modelsDataSite import DataSiteModel
from home.formHome import FormHome
from utils.logger.telegram.telegram_debug import Telegram
from utils.utils import change_number


# TODO проверить og


def index(request):
    settings_sql = DataSiteModel.objects.first()

    context = {
        'brand_name': settings_sql.brand_name,
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

    }

    response = render(request, 'index.html', context=context)

    return response


def get_order(request):
    if request.method == "POST":
        form = FormHome(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            phone = form.cleaned_data['phone']

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

    res = index(request)

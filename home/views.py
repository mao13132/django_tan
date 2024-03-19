import asyncio

from django.shortcuts import render

from home.formHome import FormHome
from utils.logger.telegram.telegram_debug import Telegram
from utils.utils import change_number

# TODO проверить og

tel = '+71111111111'

context = {
    'tel': tel,
    'instagram': '#',
    'title': 'Проверка',
    'og_url': 'localhost',
    'description': 'моментальный загар, загар Нижний Новгород, Моментальный загар в Нижнем новгороде. '
                   'Стань загорелой за 20 минут. Красивый и ровный загар в любое время года. '
                   'Обучение мастеров моментального загара',
    'keywords': 'моментальный загар эко загар автозагар солярий',
    'og_description': 'Быстро. Качественно. Профессионально.',
    'og_image': 'images/IMG_7259.PNG',
    'format_tel': change_number(tel),
    'form': FormHome(),

}


def index(request):
    if request.method == "POST":
        form = FormHome(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            phone = form.cleaned_data['phone']

            _msg = f'✅ Новая заявка {phone}%0A%0A' \
                   f'Имя: {name}%0A' \
                   f'Телефон: <code>{phone}</code>'

            asyncio.run(Telegram().new_order(_msg))

    response = render(request, 'index.html', context=context)

    return response

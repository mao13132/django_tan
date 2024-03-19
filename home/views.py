from django.shortcuts import render

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

}


def index(request):
    response = render(request, 'index.html', context=context)

    return response

# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import asyncio

from statistic.models import ClickersModule
from utils.get_ip import get_client_ip
from utils.logger._logger import logger_msg


def save_click_from_statistic(request):
    try:
        utm = '-'.join(f'{x} - {y}' for x, y in request.GET.items())
    except:
        utm = ''

    try:
        statistic = ClickersModule()

        statistic.user_agent = request.META.get('HTTP_USER_AGENT', '')

        statistic.utm = utm

        statistic.ip = get_client_ip(request)

        statistic.session_id = request.COOKIES.get('sessionid', '')

        statistic.computer_name = request.META.get('USERDOMAIN', '')

        statistic.processor_info = request.META.get('PROCESSOR_ARCHITECTURE', '')

        statistic.save()
    except Exception as es:
        asyncio.run(logger_msg(f'Ошибка при формирования контекста "{es}"'))

        return False

    return True

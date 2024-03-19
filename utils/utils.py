# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def change_number(number):
    try:
        new_number = f'{number[:2]} ({number[2:5]}) {number[5:8]}-{number[8:10]}-{number[10:12]}'
    except:
        new_number = number

    return new_number

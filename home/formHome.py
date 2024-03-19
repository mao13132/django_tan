# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from django import forms


class FormHome(forms.Form):
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'pattern': '\+{0,1}[0-9]+',
                                                                         'class': 'form-control-phone',
                                                                         'placeholder': 'Телефон'}), required=True)

    name = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control-name',
                                                                        'placeholder': 'Имя'}),
                           required=True)

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items', 'status']
        labels = {
            'table_number': 'Номер стола',
            'items': 'Список блюд (название:цена)',
            'status': 'Статус заказа',
        }

    def clean_table_number(self):
        table_number = self.cleaned_data.get('table_number')
        if not isinstance(table_number, int):
            raise forms.ValidationError('Номер стола должен быть целым числом')
        if table_number <= 0:
            raise forms.ValidationError('Номер стола должен быть положительным')
        return table_number

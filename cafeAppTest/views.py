from django.db.models import Sum, Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

def order_list(request):
    search_query = request.GET.get('search', '').lower()
    if search_query:
        orders = Order.objects.filter(Q(table_number__icontains=search_query) | Q(status__icontains=search_query))
    else:
        orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})

def order_revenue(request):
    total_revenue = Order.objects.filter(status='оплачено').aggregate(Sum('total_price'))['total_price__sum'] or 0
    return render(request, 'orders/order_revenue.html', {'total_revenue': total_revenue})

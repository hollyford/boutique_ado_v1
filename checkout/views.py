from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51INK7cBCo2us5SzrPeRDCZh5UgfnLz7g0nmARvtTYE9c7CMk2jREu7H1jhVOQZTK3QtCUIQnvZuqn9hkz69T360S0016TI25VB',
        'client_sevret': 'test client secret'
    }

    return render(request, template, context)
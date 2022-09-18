from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
import stripe
import os
from dotenv import load_dotenv
from .models import Item

load_dotenv()

stripe.api_key = os.getenv('SEC_KEY')


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        DOMAIN = r'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                'item_id': item.id
            },
            mode='payment',
            success_url=DOMAIN + '/thanks/',
            cancel_url=DOMAIN + '/index/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


def item_details(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
        'STRIPE_PUBLIC_KEY': os.getenv('PUB_KEY')
    }
    return render(request, 'main/item_details.html', context)


def index(request):
    items = Item.objects.all()
    return render(request, 'main/items_list.html', {'items': items})


def thanks(request):
    msg = 'Thanks!'
    return HttpResponse(msg, content_type='text/plain')

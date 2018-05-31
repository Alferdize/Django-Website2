from django.conf import settings

from django.shortcuts import render
import stripe
from django.contrib.auth.decorators import login_required
# Create your views here.

secretkey = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    publishkey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']

        charge = stripe.Charge.create(
            amount=999,
            currency='usd',
            description='Example charge',
            source=token,
        )
    context = {'publishkey':publishkey}
    template = 'checkout.html'
    return render(request,template,context)
 

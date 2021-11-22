import stripe
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth import logout as logout_auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Profile

stripe.api_key = settings.STRIPE_SECRET_KEY

PRICE_ID = settings.PRICE_KEY


def dashboard(request):
    """
    """
    return render(request, "dashboard.html", {"request": request})


def subscribe(request):
    """
    """
    return render(request, "subscribe.html", {"request": request})


def subscription(request):
    """
    """
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        customer = stripe.Customer.create(
            description=user.username,
            email=user.email,
            name=user.username,
            address={
                "line1": "510 Townsend St",
                "postal_code": "98140",
                "city": "San Francisco",
                "state": "CA",
                "country": "US",
            },
            source=request.POST["stripeToken"],
        )
        subs = stripe.Subscription.create(
            customer=customer.id,
            items=[
                {"price": PRICE_ID},
            ],
        )
        charge = stripe.Charge.create(
            amount="50",
            currency="usd",
            description="Payment Gateway",
            customer=customer.id,
        )
        Profile.objects.filter(user=request.user).update(
            sub_id=subs.id,
            charge_id=charge.id,
            customer_id=customer.id,
            user=request.user,
            is_pro=True,
        )
    return render(request, "dashboard.html")


def logout(request):
    """
    """
    logout_auth(request)
    return redirect("auth/login/")


def cancel_sub(request):
    """
    """
    user = Profile.objects.get(user=request.user)
    stripe.Subscription.delete(
        user.sub_id,
    )
    if user:
        Profile.objects.filter(user=request.user).update(is_pro=False)
    return redirect(reverse("subscribe_page"))

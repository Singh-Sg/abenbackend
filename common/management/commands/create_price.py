from django.core.management import BaseCommand
import stripe


class Command(BaseCommand):
    def handle(self, *args, **kwar):
        product = stripe.Product.create(name="Gold Special")

        price = stripe.Price.create(
            unit_amount=59,
            currency="usd",
            recurring={"interval": "month"},
            product=product.id,
        )
        print(price)

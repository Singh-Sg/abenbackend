from django.contrib.auth.models import User
from django.db import models

SUBSCRIPTION = (
    ("F", "FREE"),
    ("M", "MONTHLY"),
    ("Y", "YEARLY"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_pro = models.BooleanField(default=False)
    pro_expiry_date = models.DateTimeField(null=True, blank=True)
    subscription_type = models.CharField(
        max_length=100, choices=SUBSCRIPTION, default="FREE"
    )
    sub_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    charge_id = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.user.username)

from django.contrib.auth.models import AbstractUser
from django.db import models
from core import managers as core_managers
from django.shortcuts import reverse

import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string


class User(AbstractUser):

    """ Custom User Model """

    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar", blank=True)
    password = models.CharField(max_length=256)
    manageruser = models.BooleanField(default=False)
    """
    def count_reviews(self):
        all_reviews = self.reviews.all()
        return all_reviews
    """
    # objects = core_managers.CustomModelManager()

    def get_absolute_url(self):
        return reverse("users:userProfile", kwargs={"pk": self.pk})

    """
    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                _("Verify Account"),
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
            return
    """

from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


class DashboardLoginRedirectTests(TestCase):
    def setUp(self):
        self.password = "valid-test-password"
        self.user = CustomUser.objects.create_user(
            username="student",
            password=self.password,
        )

    def test_login_redirects_to_dashboard_even_when_next_is_provided(self):
        response = self.client.post(
            f"{reverse('login')}?next=/admin-panel/",
            {"username": self.user.username, "password": self.password},
        )

        self.assertRedirects(response, reverse("dashboard"), fetch_redirect_response=False)

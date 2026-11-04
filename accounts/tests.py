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


class ProfileAndSignupTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="profileuser",
            password="valid-test-password",
            role=CustomUser.Role.STUDENT,
        )

    def test_profile_updates_only_the_signed_in_user_fields(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("profile"),
            {
                "first_name": "Updated",
                "last_name": "Name",
                "email": "updated@example.com",
                "course": "Computing",
                "role": CustomUser.Role.ADMIN,
            },
        )

        self.assertRedirects(response, reverse("profile"), fetch_redirect_response=False)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Updated")
        self.assertEqual(self.user.course, "Computing")
        self.assertEqual(self.user.role, CustomUser.Role.STUDENT)

    def test_signup_shows_success_message_after_redirect_to_login(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newstudent",
                "password1": "Strong!Pass9876",
                "password2": "Strong!Pass9876",
                "first_name": "New",
                "last_name": "Student",
                "email": "newstudent@example.com",
                "role": CustomUser.Role.STUDENT,
                "course": "Computing",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your account was created. Please log in.")
        self.assertTrue(CustomUser.objects.filter(username="newstudent").exists())

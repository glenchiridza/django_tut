from django.test import TestCase
from django.shortcuts import reverse


class LandingPageTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse("landing-page"))
        print(response.content)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing_page.html")


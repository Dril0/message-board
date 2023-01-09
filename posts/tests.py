from django.test import TestCase
from .views import Posts
from django.urls import reverse

# Create your tests here.

"""cuando testeamos bases de datos se utiliza TestCase, y solo se va a testear las funciones que empiecen con test*"""


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Posts.objects.create(text="This is a Test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a Test!")

    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a Test!")

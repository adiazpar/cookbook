# Helpful resource:
# https://www.javatpoint.com/unit-testing-in-django#:~:text=Writing%20Unit%20Tests%20in%20Django&text=To%20get%20started%2C%20you'll,of%20the%20Django%20TestCase%20class.&text=In%20this%20example%2C%20we%20define,called%20%22my%2Dview%22.

from django.test import TestCase
from django.urls import reverse         # For testing views
from cookbook_app.models import Recipe  # For testing models

# ------------------------- TESTING VIEWS ------------------------- #
class HomeTestCase(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))

        # The status code should be 200 if the reverse was successful:
        self.assertEqual(response.status_code, 200)


class RegisterTestCase(TestCase):
    def test_register(self):
        response = self.client.get(reverse('register'))

        # The status code should be 302 if the reverse was successful:
        self.assertEqual(response.status_code, 200)


class LoginTestCase(TestCase):
    def test_login(self):
        response = self.client.get(reverse('login'))

        # The status code should be 200 if the reverse was successful:
        self.assertEqual(response.status_code, 200)


class RecipesTestCase(TestCase):
    def test_recipes(self):
        response = self.client.get(reverse('recipes'))

        # The status code should be 302 if the reverse was successful:
        self.assertEqual(response.status_code, 302)


# ------------------------- TESTING MODELS ------------------------ #
class RecipeTestCase(TestCase):
    def setUp(self):
        self.model = Recipe.objects.create(name='Test Recipe')

    def test_recipe_name(self):
        self.assertEqual(self.model.name, 'Test Recipe')


# ------------------------- TESTING FORMS ------------------------- #
# So I cannot test forms because I do not have a forms.py file.
# I know, it's not very scalable without using the django forms API,
# but I wanted to understand how forms worked in the first place.
# So, I manually created my own forms in views.py
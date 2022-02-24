from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class PagesTests(SimpleTestCase):

    def test_home_page_view_is_up(self):
        response = self.client.get('/pages/home/')
        self.assertEqual(response.status_code, 200)


    def test_about_page_view_is_up(self):
        response = self.client.get("/pages/about/")

    def test_home_page_view_uses_correct_template(self):
        response = self.client.get("/pages/home/")
        self.assertTemplateUsed(response, "pages/home.html")

    def test_about_page_view_uses_correct_template(self):
        response = self.client.get("/pages/about/")
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_view_uses_correct_template(self):
        response = self.client.get("/pages/about/")
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_view_has_correct_content(self):
        response = self.client.get("/pages/home/")
        self.assertContains(response, "Welcome to the home page")
    
    def test_about_page_view_has_correct_content(self):
        response = self.client.get("/pages/about/")
        self.assertContains(response, "Welcome to the about page")



    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")

    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")

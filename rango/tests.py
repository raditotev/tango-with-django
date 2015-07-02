from django.test import TestCase

from rango.models import Category
from django.core.urlresolvers import reverse
from django.test import Client

class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):

        """
                ensure_views_are_positive should results True for categories where views are zero or positive
        """
        cat = Category(name='test',views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    def test_slug_line_creation(self):
             """
             slug_line_creation checks to make sure that when we add a category an appropriate slug line is created
             i.e. "Random Category String" -> "random-category-string"
             """

             cat = Category(name='Random Category String')
             cat.save()
             self.assertEqual(cat.slug, 'random-category-string')

def add_cat(name, views, likes):
    '''
    Helper method creating test categories.
    '''
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

def test_view_index(self, string):
    '''
    Helper method for testing index page without client.
    '''
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, string)

class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        """
        If no categories exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
	    """
	    If no categories exist, an appropriate message should be displayed.
	    """
	    add_cat('test',1,1)
	    add_cat('temp',1,1)
	    add_cat('tmp',1,1)
	    add_cat('tmp test temp',1,1)
	    response = self.client.get(reverse('index'))
	    self.assertEqual(response.status_code, 200)
	    self.assertContains(response, "tmp test temp")
	    num_cats =len(response.context['categories'])
	    self.assertEqual(num_cats , 4)

    def test_index_view_for_title(self):
        test_view_index(self, "Rango - Index")

    def test_index_view_for_login(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_index_view_for_toggle_navigation(self):
        test_view_index(self, "Toggle navigation")

    def test_index_view_for_navbar_brand(self):
        test_view_index(self, "Rango")

    def test_index_view_for_home(self):
        test_view_index(self, "Home")

    def test_index_view_for_registration(self):
        test_view_index(self, "Register Here")

    def test_index_view_for_about(self):
        test_view_index(self, "About")

    def test_index_view_for_find_category(self):
        test_view_index(self, "Find a Category")

    def test_view_index_when_user_logs_in(self):
        client = Client()
        response = client.post('/accounts/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 200)

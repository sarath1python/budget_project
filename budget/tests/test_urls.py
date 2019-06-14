from django.test import SimpleTestCase
from django.urls import resolve, reverse
from budget.views import project_list, ProjectCreateView, project_detail

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):

        url = reverse('list')
        self.assertEquals(resolve(url).func, project_list)

    def test_add_url_is_resolved(self):

        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)


    def test_detail_url_is_resolved(self):

        url = reverse('detail',args='c')
        self.assertEquals(resolve(url).func, project_detail)

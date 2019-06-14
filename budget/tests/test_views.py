from django.test import Client, TestCase
from django.urls import reverse, resolve
from budget.models import Project, Category, Expense


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['project1'])
        self.project1 = Project.objects.create(
            name='project1',
            budget=10000
        )
        self.category1 = Category.objects.create(
            project=self.project1,
            name='category1'
        )

    def test_list_view_GET(self):

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    # def test_add_view_POST(self):
    #
    #
    #
    #     url = reverse('add')
    #
    #     response = self.client.get(path=url)
    #
    #     self.assertEquals(response.status_code,200)

    def test_project_detail_GET(self):

        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')

    def test_project_detail_POST_add_new_expense(self):

        response = self.client.post(self.detail_url, {
            'title':'title1',
            'amount':100,
            'category':'category1'
        })

        obj = self.project1.expenses.get(id=1)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(obj.title,'title1')
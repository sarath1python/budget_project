from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields.citext import CITextField


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()
    new_field = models.CharField(max_length=100, null=True)
    add_field = models.CharField(max_length=120, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    @property
    def budget_left(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount

        # temporary solution, because the form currently only allows integer amounts
        total_expense_amount = int(total_expense_amount)

        return self.budget - total_expense_amount

    @property
    def total_transactions(self):
        expense_list = Expense.objects.filter(project=self)
        return len(expense_list)

    def get_absolute_url(self):
        return '/'+ self.slug;


class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    new_field = models.CharField(max_length=100, null=True)


class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title1 = models.CharField(max_length=100)

    class Meta:
        ordering = ('-amount',)

class users(models.Model):
    name = models.CharField(max_length=100)
    place = CITextField()



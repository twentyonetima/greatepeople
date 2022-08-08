from django.db import models

# Create your models here.
from django.urls import reverse


class Men(models.Model):
    name = models.CharField('Name', max_length=255)
    last_name = models.CharField('Last name', max_length=255)
    content = models.TextField('Discription')
    photo = models.ImageField('Photo', upload_to='photos/%Y/%m/%d')
    year_of_birth = models.PositiveSmallIntegerField('Year of birth', default=1990)
    year_of_death = models.PositiveSmallIntegerField('Year of death', blank=True, null=True)
    age = models.PositiveSmallIntegerField('Age', default=32)
    time_create = models.DateTimeField('Time create', auto_now_add=True)
    time_update = models.DateTimeField('Time update', auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        full_name = self.name + ' ' + self.last_name
        return full_name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Man'
        verbose_name_plural = 'Men'


class Category(models.Model):
    name = models.CharField('Category', max_length=100, db_index=True)
    description = models.TextField("Description", null=True)
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

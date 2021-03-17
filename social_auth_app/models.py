from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=75, blank=True)
    birth_date = models.DateField(null=True, blank=True,
                                  verbose_name='Дата рождения')
    bio = models.TextField('О себе', blank=True)
    city = models.CharField('Город', max_length=150, blank=True)
    avatar = models.ImageField(upload_to='media',
                               default='default/default.png',
                               blank=True, verbose_name='Аватар')

    class Meta:
        ordering = ['-date_joined']

    def get_info(self):
        fields = ('first_name', 'middle_name', 'last_name',
                  'birth_date', 'email', 'city')
        response = []
        for field in fields:
            field_object = self._meta.get_field(field)
            response.append({
                'name': field_object.verbose_name,
                'value': field_object.value_from_object(self)
            })
        return response

from django.db import models

class Contact(models.Model):
    contact_first_name = models.CharField('Имя', max_length = 50)
    contact_last_name = models.CharField('Фамилия', max_length = 50)
    contact_email = models.CharField('E-mail адрес', max_length = 50)
    contact_massage = models.TextField('Текст сообщения')

    def __str__(self):
        return self.contact_first_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

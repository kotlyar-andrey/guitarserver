from django.db import models


OS_VARIANTS = (
    (0, 'Android'),
    (1, 'iOs'),
    (2, 'Other'),
)


class MobileUser(models.Model):
    uuid = models.UUIDField(verbose_name="UUID")
    email = models.EmailField(unique=True, blank=True, null=True)
    os = models.IntegerField(verbose_name="os", choices=OS_VARIANTS)
    created_on = models.DateTimeField(verbose_name='Дата/время регистрации', auto_now_add=True)

    class Meta:
        verbose_name = 'Мобильный пользователь'
        verbose_name_plural = 'Мобильные пользователи'

    def __str__(self):
        return f'User {self.uuid}'


class Payment(models.Model):
    mobile_user = models.ForeignKey(MobileUser, verbose_name='Пользователь', related_name='payments', null=True,
                                    on_delete=models.SET_NULL)
    info = models.JSONField(verbose_name='Вся информация об оплате')
    created_on = models.DateTimeField(verbose_name='Дата/время создания записи об оплате', auto_now_add=True)

    class Meta:
        verbose_name = 'Оплата пользователя'
        verbose_name_plural = 'Оплаты пользователя'

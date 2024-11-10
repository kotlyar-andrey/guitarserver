from django.db import models


OS_VARIANTS = (
    (0, 'Android'),
    (1, 'iOs'),
    (2, 'Other'),
)

PRODUCT_TYPES = (
    (0, 'product'),
    (1, 'subscription'),
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
    product_type = models.IntegerField(verbose_name="Тип продукта", choices=PRODUCT_TYPES, default=0)
    product_id = models.CharField(verbose_name="Название продукта", blank=True, max_length=200)
    transaction_id = models.CharField(verbose_name="ID транзакции", blank=True, max_length=100)
    checked = models.BooleanField(verbose_name="Проверенная покупка", default=False)
    info = models.JSONField(verbose_name='Вся информация об оплате')
    created_on = models.DateTimeField(verbose_name='Дата/время создания записи об оплате', auto_now_add=True)

    class Meta:
        verbose_name = 'Оплата пользователя'
        verbose_name_plural = 'Оплаты пользователей'

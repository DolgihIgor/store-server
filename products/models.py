from django.db import models


class ProductCategory(models.Model):
    """
    Модель для категорий, поле name должно быть уникальным.
    Поле описание необязательно для заполнения.
    Поле id создается Django автоматически с автоинкрементом.
    """
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Модель для товаров """
    name = models.CharField(max_length=256)
    description = models.TextField()

    # Поле с ценой, 6 знаков до запятой, 2 знака после
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Количество, положительное, по умолчанию 0
    quantity = models.PositiveIntegerField(default=0)

    # Изображение, загружается в папку products_images
    # для работы с изображениями необходимо установить пакет Pollow
    image = models.ImageField(upload_to='products_images')

    # Категории - это ссылка на категорию, при удалении категории,
    # CASCADE - каскадное удаление всех товаров с этой категорией
    # если указать PROTECT - не даст удалить, пока существует ссылка на категорию
    # SET_DEFAULT, default = Null - заполнит по умолчанию нулями
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

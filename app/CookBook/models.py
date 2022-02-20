from django.db import models


class Recipes(models.Model):
    'Модель рецептов'
    title = models.CharField(max_length=150, verbose_name='Название блюда')
    text_recipe = models.TextField(verbose_name='Рецепт')
    date_created = models.DateField(auto_now=True, verbose_name='Дата создания')
    photo_food = models.ImageField(blank=True, verbose_name='Фото блюда', upload_to='photo_food/%Y-%m-%d')
    ingredients = models.ManyToManyField('Ingredients')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=150, unique=True, verbose_name='Ингредиент')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.ingredient

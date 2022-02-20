# Generated by Django 4.0.2 on 2022-02-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=150, verbose_name='Ингредиент')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название блюда')),
                ('text_recipe', models.TextField(verbose_name='Рецепт')),
                ('date_created', models.DateField(auto_now=True, verbose_name='Дата создания')),
                ('photo_food', models.ImageField(blank=True, upload_to='photo_food/%Y-%m-%d', verbose_name='Фото блюда')),
                ('ingredients', models.ManyToManyField(to='CookBook.Ingredients')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
    ]
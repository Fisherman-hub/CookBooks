from django.contrib import admin
from .models import Recipes, Ingredients


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text_recipe', 'date_created', 'photo_food')


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('ingredient',)


admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
from django.views.generic import ListView, CreateView
from .models import Recipes, Ingredients


class Home(ListView):
    paginate_by = 5
    model = Recipes
    template_name = 'CookBook/home.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ingredients'] = Ingredients.objects.all()
        context['title'] = 'Главная страница'
        return context


class FilterRecipes(ListView):
    model = Recipes
    template_name = 'CookBook/home.html'
    context_object_name = 'ingredients'
    allow_empty = False

    def get_queryset(self):
        return Recipes.objects.filter(ingredient__pk=self.kwargs['ingredient_pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredients.objects.all()
        context['title'] = str(context['ingredients'][0].ingredient)
        context['ingredients_selected'] = context['ingredients'][0].ingredient_pk
        return context


class RecipesForm(CreateView):
    pass
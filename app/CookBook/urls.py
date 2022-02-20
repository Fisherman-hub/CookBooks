from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Home, FilterRecipes, RecipesForm

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<int:ingredient_pk>/', FilterRecipes.as_view(), name='filter_recipes'),
    path('add_recipe/', RecipesForm.as_view(), name='add_recipe'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
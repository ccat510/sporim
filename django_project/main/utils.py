from django.db.models import Count

from .models import *


bright_colors = ['#FF5733', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#FF0000', '#FF4500', '#FFD700', '#008000', '#0E6EB8', '#0E6EB8', '#483D8B', '#9400D3', '#8A2BE2']
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить спор", 'url_name': 'add_page'},
        {'title': "Список игроков", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 2

    def __init__(self):
        self.request = None

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = User.objects.annotate(Count('first_name'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

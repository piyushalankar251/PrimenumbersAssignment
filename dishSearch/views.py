from django.shortcuts import render
from django.views import View
from fuzzywuzzy import fuzz

from .models import Dish

class search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = []
        if query:
            dishes = Dish.objects.all()
            for dish in dishes:
                items = {k.lower(): v for k, v in dish.items.items()}
                for item in items.keys():
                    if fuzz.ratio(query.lower(), item) > 80:  # adjust this value as needed
                        results.append({
                            'restaurant': dish.name,
                            'item': item,
                            'price': items[item]
                        })
        return render(request, 'search.html', {'results': results})

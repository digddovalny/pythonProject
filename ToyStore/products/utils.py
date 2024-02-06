from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from products.models import Products


def query_search(query):
    # поиск по id
    if query.isdigit() and len(query) <= 4:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    return Products.objects.annotate(rank=SearchRank(vector, query).order_by("-rank"))

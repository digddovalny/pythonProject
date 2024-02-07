from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

from products.models import Products


def query_search(query):
    # поиск по id
    if query.isdigit() and len(query) <= 4:
        return Products.objects.filter(id=int(query))

    # поиск по имени и описанию
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    res = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

    res = res.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel="<span style='background-color: yellow;'>",
            stop_sel="</span>",
        )
    )

    res = res.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel="<span style='background-color: yellow;'>",
            stop_sel="</span>",
        )
    )
    return res

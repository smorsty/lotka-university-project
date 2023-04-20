from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article, Author, Connection
from .forms import FullSearch, CategoryFilterForm


def home(request):
    return render(request, 'home.html')


def article_list_by_parameter(request, parameter: str):
    if parameter.isdigit():
        parameter = int(parameter)
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         f"SELECT aaa.id, aaa.year, aaa.category, aaa.name, aaa.link, aaa2.name FROM article_app_article aaa, article_app_author aaa2, article_app_connection aac WHERE aac.article_id = aaa.article_id AND aac.author_id = aaa2.author_id and aaa.year = {parameter}")
        #     rows = cursor.fetchall()
        articles_list = Article.objects.all().filter(year=parameter)
    else:
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         f"SELECT aaa.id, aaa.year, aaa.category, aaa.name, aaa.link, aaa2.name FROM article_app_article aaa, article_app_author aaa2, article_app_connection aac WHERE aac.article_id = aaa.article_id AND aac.author_id = aaa2.author_id and aaa.category = {parameter}")
        #     rows = cursor.fetchall()
        articles_list = Article.objects.all().filter(category=parameter, year__gte=2022)[:50]

    # articles = {}
    # n = len(rows)
    # for i in range(n):
    #     # print(type(rows[i]), rows[i])
    #     id = str(rows[i][0])
    #     if id not in articles:
    #         articles[id] = {}
    #         articles[id]['id'] = rows[i][0]
    #         articles[id]['year'] = rows[i][1]
    #         articles[id]['category'] = rows[i][2]
    #         articles[id]['article_name'] = rows[i][3]
    #         articles[id]['link'] = rows[i][4]
    #         articles[id]['authors_names'] = str(rows[i][5])
    #     else:
    #         articles[id]['authors_names'] += ", " + str(rows[i][5])
    # # print(articles)
    paginator = Paginator(articles_list, 100)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'article_list.html', {'articles': articles})


def article_info(request, id: str):
    article_id = int(id)
    authors_id = Connection.objects.all().filter(article_id=article_id).values('author_id')
    authors = Author.objects.all().filter(author_id__in=authors_id)

    return render(request, 'article_info.html', {'authors': authors})


def article_list_per_author(request, cur_id: str):
    article_id = int(cur_id)
    articles_ids = Connection.objects.filter(author_id=article_id).values('article_id')
    articles = Article.objects.filter(article_id__in=articles_ids)

    return render(request, 'article_list.html', {'articles': articles})


def search_form(request):
    if request.POST:
        main_form = FullSearch(request.POST)
        category_form = CategoryFilterForm(request.POST)
        if main_form.is_valid() and category_form.is_valid():
            query = main_form.cleaned_data['keyword']
            author_name = main_form.cleaned_data['authors']
            start_year = main_form.cleaned_data['start_year']
            end_year = main_form.cleaned_data['end_year']
            categories = category_form.cleaned_data['categories']

            if not categories:
                categories = ['Foundations',
                              'Secret-key cryptography',
                              'Cryptographic protocols',
                              'Public-key cryptography',
                              'Applications',
                              'Implementation',
                              'Attacks and cryptanalysis',
                              'Uncategorized',
                              ]

            authors_id = Author.objects.filter(name__icontains=author_name).values('author_id')
            articles_by_author = Connection.objects.filter(author_id__in=authors_id).values('article_id')
            articles = Article.objects.filter(
                name__icontains=query,
                category__in=categories,
                year__range=[start_year, end_year],
                article_id__in=articles_by_author,
            )[:50]
            return render(request, 'article_list.html', {'articles': articles})
    else:
        main_form = FullSearch()
        category_filter = CategoryFilterForm()

    return render(request, 'search.html', {'form': main_form, 'category_filter': category_filter})


def author_list(request):
    # author1 = Author.objects.get(author_id=312)
    # author2 = Author.objects.get(author_id=12700)
    authors = Author.objects.all().filter(author_id__gte=12000)[:20]
    return render(request, 'author_list.html', {'authors': authors})
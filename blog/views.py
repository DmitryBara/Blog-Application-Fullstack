import uuid

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from blog.models import Article
from blog.forms import ArticleForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse





# Test For user_passes_test @decorator
# def owner_of_article(user, article_id):
#     user_articles = Article.objects.filter(author_id=user.id, id=article_id)
#     if user_articles:
#         return True
#     else:
#         return False

# My Articles from "Personal Account" block
@login_required
def my_articles(request):
    if request.method == 'GET':
        forms = dict ()
        user = request.user
        user_articles = Article.objects.filter(author_id=user.id).order_by('-pub_date')
        for article in user_articles:
            forms[article.id] = ArticleForm(instance=article)
        return render(request, 'pa_my_articles.html', {'user_articles': user_articles, 'forms': forms})


def one_article (request, article_id):
    try:
        article = Article.objects.filter(hiden=False).get(id=article_id)
    except Article.DoesNotExist:
        raise Http404('Статья удалена, скрыта или никогда не существовала')

    context = {'article': article, 'user': request.user}
    return render(request,'kod_blog_one.html', context)



def all_articles (request):
    #catch get params from url if it exist (limit, page)
    limit = int(request.GET.get('limit', 9))
    page = int(request.GET.get('page', 1))
    articles = Article.objects.all().order_by('-pub_date').filter(hiden=False)

    try:
        last_article = articles[0]
        articles = articles[1:]
    except IndexError:
        last_article = None
        articles = [None]

    paginator = Paginator(articles, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)

    context = {
        'last_article':     last_article,
        'paginator':        paginator,
        'page':             page,              
    }
    return render(request, 'kod_blog_all_articles.html', context)



@login_required
def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author_id = request.user.id
            article.uuid = request.session['a_uid']
            article.save()
            url = article.get_url()
            return HttpResponseRedirect(url)

    else:
        form = ArticleForm()
        request.session['a_uid'] = uuid.uuid4().hex
    context= {'form': form, 'user': request.user}
    return render(request, 'kod_add.html', context)



def edit_article (request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        request.session['a_uid'] = article.uuid
    except Article.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article, article_id=article_id)
        if form.is_valid():
            article = form.save()
            url = article.get_url()
            return HttpResponseRedirect(url)

    else:
        form = ArticleForm(instance=article)
    context = { 'article': article, 'form': form}
    return render(request, 'kod_edit.html', context)



def change_visible (request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        state_now = article.hiden
    except Article.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article, article_id=article_id)
        if form.is_valid():
            article = form.save(commit=False)
            article.hiden = not state_now
            article.save()
            url = reverse('my_articles')
            return HttpResponseRedirect(url)



def delete_article (request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404
    article.delete()
    url = reverse('my_articles')
    return HttpResponseRedirect(url)








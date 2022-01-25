from django.http import Http404
from django.shortcuts import render
from django.views import generic

from apps.articles.models import Article


class ArticlelistView(generic.TemplateView):
    template_name ='article_list.html'


    def get_context_data(self, **kwargs):
        context = dict()
        context['article_list'] = Article.objects.all()
        return context


class ArticleDetaView(generic.TemplateView):
    template_name = 'article_datel.html'


    def get_context_data(self,**kwarsd):
       context = dict()
       article_pk = kwarsd['pk']
       try:
         context['article']=Article.objects.get(id=article_pk)
       except Article.DoesNotExist:
           raise Http404
       return context

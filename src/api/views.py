import json
from api.models import Author, Article
from rest_framework import viewsets
from api.serializers import AuthorSerializer, ArticleSerializer
from django.http import HttpResponse


class AuthorViewSet(viewsets.ModelViewSet):
    """ Endpoint to consume Author data
    """
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """ Endpoint to consume Articler data
    """
    queryset = Article.objects.all().order_by('-published_date')
    serializer_class = ArticleSerializer


def index(request):
    """ The index page
    """
    data = {'where_am_i': "You're at Cruncher! More information on https://github.com/perylemke/cruncher",
            'author': "Pery Lemke",
            'author_email': 'pery.lemke@gmail.com',
            'author_twitter': 'https://twitter.com/perylemke'}
    return HttpResponse(json.dumps(data), content_type='application/json', charset='utf-8')

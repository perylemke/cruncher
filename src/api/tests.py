import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Author, Article


class APIViewsAuthor(APITestCase):
    fixtures = ['api_author_data.json']

    def test_authors(self):
        resp = self.client.get('/api/v1/authors/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_authors_detailed(self):
        resp = self.client.get('/api/v1/authors/1/')
        data = {'id': 1,
                'name': 'Ron Miller',
                'profile_page': 'https://techcrunch.com/author/ron-miller/',
                'twitter_page': 'https://twitter.com/ron_miller'}
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, data)


class APIViewsArticle(APITestCase):
    fixtures = ['api_author_data.json', 'api_article_data.json']

    def test_articles(self):
        resp = self.client.get('/api/v1/articles/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_articles_detailed(self):
        resp = self.client.get('/api/v1/articles/1/')
        data = {'id': 1,
                'title': "Why AWS has such a big lead in the cloud",
                'content': 'This is a brief content!',
                'url': 'https://techcrunch.com/2017/02/13/why-aws-has-such-a-big-lead-in-the-cloud/,
                'published_date': '2017-02-13T18:20:00Z',
                'thumbnail_url': '',
                'author': 'http://testserver/api/v1/authors/1/'}

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, data)


class IndexView(APITestCase):

    def test_index(self):
        resp = self.client.get('/')
        data = {'where_am_i': "You're at Cake! More information on https://github.com/perylemke/cruncher",
                'author': "Pery Lemke",
                'author_email': 'pery.lemke@gmail.com',
                'author_twitter': 'https://twitter.com/perylemke'}

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.content.decode(), json.dumps(data))


class AuthorModelTest(TestCase):

    def test_string_method(self):
        author = Author(name='Eduardo Spohr')
        self.assertEqual(str(author), author.name)


class ArticleModelTest(TestCase):

    def test_string_method(self):
        article = Article(title='A Batalha do Apocalipse: Da Queda dos Anjos ao Crepúsculo do Mundo')
        self.assertEqual(str(article), article.title)

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from datetime import datetime
from django.views.decorators.csrf import ensure_csrf_cookie
import json

from webapp.models import Article

def echo_view(request, *args, **kwargs):
    # print(request.body)
    # print(json.loads(request.body))
    response_data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method
    }
    if request.body:
        response_data['content'] = json.loads(request.body)

    response_data_json = json.dumps(response_data)
    response = HttpResponse(response_data_json)
    response['Content-Type'] = 'application/json'
    return  response


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def article_view(request, *args, **kwargs):
    if request.method == "GET":
        # article_data = []
        # for article in Article.objects.all():
        #     article_data.append({
        #         'title': article.title,
        #         'content': article.content
        #     })
        article_data = list(Article.objects.values('title', 'content'))
        return JsonResponse(article_data, safe=False)
    elif request.method == "POST":
        request_data = json.loads(request.body)
        
        article = Article.objects.create(**request_data)
        return JsonResponse({'id': article.pk})
    return HttpResponseNotAllowed(['GET'])
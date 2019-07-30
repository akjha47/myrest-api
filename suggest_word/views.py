from django.shortcuts import render
from django.http import HttpResponse
from .suggest_word_helper.suggest_word_helper import words_tree

def return_response(request):
    if request.GET.get('word'):
        returned_suggestions=words_tree.return_auto_suggestions(request.GET.get('word'))
    else:
        returned_suggestions=["Sorry we can not serve you! ..Please make a GET request with Query Parameter \"word\""]
    return HttpResponse(str(returned_suggestions))

# Create your views here.

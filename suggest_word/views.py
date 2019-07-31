from django.shortcuts import render
from django.http import HttpResponse
from .suggest_word_helper.suggest_word_helper import words_tree
import re
import json
def return_response(request):
    if request.GET.get('word'):
        filtered_word = re.sub('[^A-Za-z]+', '', request.GET.get('word'))
        res_to_send={"key":filtered_word,"values":words_tree.return_auto_suggestions(filtered_word)}
    else:
        res_to_send = {"error":"Sorry we can not serve you! ..Please make a GET request with Query Parameter \"word\""}
    return HttpResponse(json.dumps(res_to_send))

# Create your views here.

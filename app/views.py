from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def warmup_one_view(response: HttpResponse, number):
    if abs(100 - number) <= 10:
        return HttpResponse(True)
    elif abs(200 - number) <= 10:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def warmup_two_view(response: HttpResponse, word):
    sploded_word = ""

    for letter in range(0, len(word)):
        sploded_word += word[: letter + 1]
    return HttpResponse(sploded_word)


def cat_dog_view(response: HttpResponse, string):
    cat_count = string.count("cat")
    dog_count = string.count("dog")

    if cat_count == dog_count:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def logic_two_view(response: HttpResponse, numberA, numberB, numberC):
    add_list = []
    dupe_list = []

    for i in (numberA, numberB, numberC):
        if i not in add_list:
            add_list.append(i)
        else:
            dupe_list.append(i)

    for i in dupe_list:
        if i in add_list:
            add_list.remove(i)

    return HttpResponse(sum(add_list))

from django.shortcuts import render
from django.http import HttpResponseNotFound


def main_view(request):

    return render(request, 'tours/index.html')


def departure_view(request, departure):

    return render(request, 'tours/departure.html')


def tour_view(request, ident):

    return render(request, 'tours/tour.html')


def my_handler404(request, exception):
    return HttpResponseNotFound('Вы что-то не то ввели...=(')


def my_handler500(request):
    return HttpResponseNotFound('Ошибка на стороне сервера...=(')

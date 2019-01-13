from django.shortcuts import render

from django.http import HttpResponse


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return HttpResponse('Hello world!')
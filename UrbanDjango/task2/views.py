from django.shortcuts import render
from django.views.generic import TemplateView


def main_page(request):
    return render(request, 'main_page.html')


def func_page(request):
    return render(request, 'func_page.html')


class class_page(TemplateView):
    template_name = 'class_page.html'

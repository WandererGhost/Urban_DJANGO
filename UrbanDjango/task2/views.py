from django.shortcuts import render
from django.views.generic import TemplateView

def main_page(request):
    return render(request, 'main.html')


def func_view(request):
    return render(request, 'func_view.html')


class class_view(TemplateView):
    template_name = 'class_view.html'

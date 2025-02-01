from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import UserRegister
from .models import *


def main_page(request):
    return render(request, 'main_page.html')


def order(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'place_an_order.html', context)


def goods(request):
    return render(request, 'basket.html')


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                if Buyer.objects.filter(name=username).exists():
                    info['error'] = 'Покупатель уже существует'
                else:
                    buyer = Buyer.objects.create(name=username, balance=0.00, age=age)
                    return render(request, 'registration_page.html', {'message': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page.html', info)


def news_pages(request):
    posts = News.objects.all().order_by('-date')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})

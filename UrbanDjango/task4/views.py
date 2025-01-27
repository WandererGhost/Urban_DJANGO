from django.shortcuts import render


def get_contact_task4(request):
    return render(request, 'contacts4.html')


def order_task4(request):
    services = [
        'Печать документов',
        'Печать фотографий',
        'Печать на кружках',
        'Изготовление визиток',
        'Широкоформатная печать'
    ]
    context = {
        'services': services
    }
    return render(request, 'place_an_order4.html', context)

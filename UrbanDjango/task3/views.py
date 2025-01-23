from django.shortcuts import render


def get_contact(request):
    return render(request, 'contacts.html')


def order(request):
    p1 = 'Печать документов'
    p2 = 'Печать фотографий'
    p3 = 'Печать на кружках'
    p4 = 'Изготовление визиток'
    p5 = 'Широкоформатная печать'
    context = {
        'p1': p1,
        'p2': p2,
        'p3': p3,
        'p4': p4,
        'p5': p5
    }
    return render(request, 'place_an_order.html', context)

from django.shortcuts import render


def hello(request):
    arr = ["Oded", "Shachar", "Egor", "Gidon", "Liat", "Almog"]
    context = {"users": arr, "admin": "Bogdan"}
    return render(request, 'hello/index.html', context)

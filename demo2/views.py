from django.shortcuts import render
from django.http import HttpResponse
from demo2.models import Order

def main(request):
    tovar = Order.objects.all().order_by('klient')


    context = {
        'pr': tovar,
    }

    return render(request, "base.html", context)
    #  return render(request, "base.html")


def filtr(request):
    name = request.POST.get("client")
    tovar = Order.objects.filter(klient=name)

    context = {
        'pr': tovar,
    }

    return render(request, "base.html", context)

def search(request):
    if request.method == "POST":
        name = request.POST.get("stroka")
        # SELECT...WHERE number LIKE '%pattern%';
        tovar = Order.objects.filter(number__contains=str(name))
        if not tovar:
            stroka = 'По вашему запросу ничего не найдено! Попробуйте искать по полю <Телефон>'
            context = {
                'stroka': stroka,
                'pr': tovar,
            }

            return render(request, "base.html", context)
        else:
            context = {
                'pr': tovar,
            }

            return render(request, "base.html", context)
    else:
        return HttpResponse(status=500)


def sort(request):
    if request.method == "POST":
        name = request.POST.get("pole")
        valuee = request.POST.get("valuee")
        if valuee == '1':
            tovar = Order.objects.all().order_by(f'{name}')
            context = {
                'pr': tovar,
            }

            return render(request, "base.html", context)
        elif valuee == '0':
            tovar = Order.objects.all().order_by(f'-{name}')
            print('-----')
            for i in tovar:
                print(i)

            context = {
                'pr': tovar,
            }
            return render(request, "base.html", context)
        else:
            return HttpResponse(status=500)
    return HttpResponse(status=500)
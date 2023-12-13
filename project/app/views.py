from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, NewsForm

from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm,CreateForm


def news(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published')
        category = request.POST.get('category')
        return HttpResponse(f'Новость {title}<br>'
                            f'Контент {content} <br>'
                            f'Вид {is_published}, {category}')
    else:
        form = NewsForm()
        return render(request, 'app/news.html', context={'form': form})


def index(request):
    if request.method == "POST":
        title = request.POST.get('name')
        content = request.POST.get('age')
        is_published = request.Post.get('is_published')
        category = request.POST.get('category')
        return HttpResponse(f'Новость {title}<br>'
                            f'Контент {content} <br>'
                            f'Вид {is_published}')
    else:
        form = UserForm()
        return render(request, 'app/index.html', context={'form': form})



def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')

        return HttpResponse(f'name {name}<br>'
                            f'email {email}<br>'
                            f'phone {phone}<br>'
                            f'service {service}<br>')

    else:
        return render(request, 'app/appointment.html')



def user_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        country = request.POST.get('country')
        city = request.POST.get('city')
        street = request.POST.get('street')
        building = request.POST.get('building')
        apartment = request.POST.get('apartment')
        return HttpResponse(f'''
        {name} {surname} {email} Проверьте адрес доставки:<br>
        {country}<br>
        {city}<br>
        {street} {building} {apartment}<br>
        ''')

    else:
        form=CreateForm()
        return render(request, 'app/createUser.html',context={'form':form})





def user(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    return HttpResponse(f'User {name},Age {age}')

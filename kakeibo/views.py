from django.shortcuts import render
from . forms import KakeiboForm # import KakeiboForm 
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . models import Category, Kakeibo
from django.db.models import Sum

class KakeiboListView(ListView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_list.html'

    def queryset(self):
        return Kakeibo.objects.all()

class KakeiboCreatView(CreateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeibo:create_done')

def create_done(request):
    return render(request, 'kakeibo/create_done.html')

class KakeiboUpdateView(UpdateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeibo:update_done')

def update_done(request):
    return render(request, 'kakeibo/update_done.html')

class KakeiboDeleteView(DeleteView):
    model = Kakeibo
    success_url = reverse_lazy('kakeibo:delete_done')

def delete_done(request):
    return render(request, 'kakeibo/delete_done.html')

def show_circle_grahp(request):
    Kakeibo_data = Kakeibo.objects.all()

    #Show total amount (sums)
    total = 0
    for item in Kakeibo_data:
        total += item.money

    category_list = []
    category_data = Category.objects.all()
    
    for item in category_data:
        category_list.append(item.category_name)

    category_dict = {}

    for i,item in enumerate(category_list):
        category_total = Kakeibo.objects.filter(category__category_name=category_list[i])\
            .aggregate(sum=Sum('money'))['sum']

        if category_total !=None:
            ratio = int((category_total / total) *100)
            category_dict[item] = ratio
        else:
            ratio = 0
            category_dict[item] = ratio

    return render(request, 'kakeibo/kakeibo_circle.html',{'category_dict': category_dict,})

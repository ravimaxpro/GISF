from django.shortcuts import render
from .forms import CommentForm,ChoiceForm,ProductFormvalidateForm,product_form
from .models import Car

# Create your views here.
def FormWidgets_view(request):
    form = CommentForm(request.POST)
    #print(form)
    if form.is_valid():
        print('is valid')
        form.save()
        form = CommentForm()
    contaxt = {
        'form': form
    }

    return render(request, "FormWidget.html", contaxt)

def CarsModelFormDisplay_view(request):
    obj = Car.objects.all()
    contaxt = {
        'obj': obj
    }

    return render(request, "CarModeldetail.html", contaxt)

def ChoiceForm_view(request):
    form = ChoiceForm()
    if form.is_valid():
        form.save()
        form = CommentForm()
    contaxt = {
        'form': form
    }
    return render(request,"ChoiceField.html",contaxt)

def ProductFormvalidate_view(request):
    form = ProductFormvalidateForm()
    print(form)
    if form.is_valid():
        form=ProductFormvalidateForm(request.POST)
        form.save()
        form = ProductFormvalidateForm()
    contaxt={
        'form':form
    }
    return render(request,'Product_create_Formvalidate.html',contaxt)
def product2_views(request):
    form=product_form
    if request.method=='POST':
        form=product_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form=product_form
    return render(request,'Product_create_Formvalidate.html',{'form':form})
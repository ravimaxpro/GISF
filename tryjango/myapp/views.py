from django.shortcuts import render,get_object_or_404
from .models import Product1,Product,departments1
from django.http import HttpResponse
from myapp.forms import MyProductModelForm
from .cal import cal

# Create your views here.

def homepage(request):
    return HttpResponse('<h1> Hello Jango, THis is project batch</h1>')

def homehtml(request):
    return render(request, 'homepage.html',{})

def BootStrap(request):
    return render(request, 'BootStrapTest.html',{})

def rawHtml(request):
    my_contant = {
        "my-text": "This is Abount Us",
        "my_number": 123,
        "my_list": [123, 234, 234]
    }
    return render(request, 'RawHtmlRender.html', my_contant )

def product_detail_view(request):
    obj=Product1.objects.get(id=1)
    contaxt={
        "title":obj.title,
        "description":obj.description
    }
    return render(request,'detail.html',contaxt)

def product_Rawcreate_view(request):
    # print(request.GET)
    # print(request.POST)
    my_title = request.POST.get('title')
    p_description = request.POST.get('description')
    p_price = request.POST.get('price')
    print('price', p_price)

    if request.method == 'POST':
        Product.objects.create(title=my_title, description=p_description,price=p_price, )  ## this will post data ro database
    contaxt = {}
    return render(request, "product_raw_create.html", contaxt)

def Product_object_list_view(request):
    queryset = Product.objects.all()
    queryset1 = departments1.objects.all()

    contaxt = {
        "objectList": queryset,
        "department": queryset1
    }

    return render(request, "prod_list.html", contaxt)

def Product_update_view(request, **kwargs):
    my_id = kwargs.get("my_id")
    if request.method == 'GET':
        obj = get_object_or_404(Product, id=my_id)

        print('obj',obj.title)
        print('obj',obj.price)

    my_title=request.POST.get('title')
    p_description=request.POST.get('description')
    p_price=request.POST.get('price')
    print('price',p_price)
    if request.method=='POST':
        my_title = request.POST.get('title')
        p_description = request.POST.get('description')
        p_price = request.POST.get('price')
        print('price', p_price)
        obj=Product.objects.filter(id=1).update(title=my_title, description=p_description, price=p_price,sumarry="default sumarry")

    contaxt = {
            "obj" : obj
    }

    return render(request, "prod_raw_update.html", contaxt)


def product_ModelForm_create_view(request):
    form = MyProductModelForm(request.POST)

    if form.is_valid():
        #form.save()
        instance=form.save(commit=False)
        print(instance.title)
        instance.save()
        form=MyProductModelForm()

    contaxt = {
        'form': form
    }

    return render(request, "Prod_ModelForm_Create.html",contaxt)

def prod_ModelForm_CRUD_view(request):
    pmessage=''
    calcValue=0
    OperationAllowed='Create'
    print('request.POST',request.POST)
    form = MyProductModelForm()
    if request.method == 'GET':
        search_id=request.GET.get('sid')
        if search_id !='None':
           try:
                Session=Product1.objects.get(id=request.GET.get('sid'))
                form=MyProductModelForm(instance=Session)
                OperationAllowed='UD'
           except Product1.DoesNotExist:
               form=MyProductModelForm()
           contaxt={
                'form':form,
                'message':'Enter invalid id'
           }
           return render(request,"prod_ModelForm_CRUD_operation.html",contaxt)

    if request.method in ['POST']:
        if 'delete' in request.POST:
            #Session = product1.Objects.get(title=request.POST.get('title'))# if title matches multiple records it throws error
            Session = Product1.objects.filter(title=request.POST.get('title'))# if title matches multiple records it return and delete
            Session.delete()
            pmessage='Recorded deleted..'
            form=MyProductModelForm()
        elif 'Create' in request.POST:
            form=MyProductModelForm(request.POST)
            print('form',form)
            if form.is_valid():
                form.save()
                pmessage='Data stored..'
                form=MyProductModelForm()
        elif 'Update' in request.POST:
            Session=Product1.objects.get(id=request.GET.get('sid'))
            form=MyProductModelForm(request.POST,instance=Session)
            if form.is_valid():
                form.save()
                pmessage="Data Updated.."
                form=MyProductModelForm()
        elif 'calc' in request.POST:
            #Session = Product1.objects.get(id=request.GET.get('Sid'))
            form = MyProductModelForm(request.POST)
            #if form.is_valid():
            calcValue = 2*2
            print('calculateValue', calcValue)
        print('OperationAllowed', OperationAllowed)
        contaxt={
            'form': form,
            'pmessage': pmessage,
            'calcValue' : calcValue,
            'OperationAllowed': OperationAllowed
    }
    return render(request,"prod_ModelForm_CRUD_operation.html",contaxt)




def caluate_view(request):
    p = 0
    r = 0
    t = 0
    cal_val = 0

    print(request.POST)
    if request.method in ['POST']:
        if 'Calc' in request.POST :
            print('datatype', type(request.POST.get('Price')))
            p = request.POST.get('Price')
            r = request.POST.get('Rate')
            t = request.POST.get('Time')
            cal_val = cal(int(p), int(t), float(r))

            print('cal_val1', cal_val)
        elif 'save' in request.POST:
            p = request.POST.get('Price')
            r = request.POST.get('Rate')
            t = request.POST.get('Time')
            cal_val = cal(int(p), int(t), float(r))
            #prt.objects.create(p,t,r,cal_val)
            print('calc values Before Rein', p,t,r,cal_val)
            p = 0
            r = 0
            t = 0
            cal_val = 0

    context = {
        'p': p,
        'r': r,
        't': t,
        'cal_val': cal_val
    }

    return render(request, 'Interestcalculation.html', context)






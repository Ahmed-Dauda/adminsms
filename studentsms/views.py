from django.shortcuts import render, HttpResponse,redirect, get_list_or_404
from studentsms.models import students_reg
from studentsms.forms import studentsform
from studentsms.filters import StudentsFilter

# Create your views here.

def index(request):
    
    posts = students_reg.objects.order_by('-created_date')
    jss1 = students_reg.objects.filter(level__exact='JSS1').count()
    jss2 = students_reg.objects.filter(level__exact='JSS2').count()
    jss3 = students_reg.objects.filter(level__exact='JSS3').count()
    ss1 = students_reg.objects.filter(level__exact='SS1').count()
    ss2 = students_reg.objects.filter(level__exact='SS2').count()
    ss3 = students_reg.objects.filter(level__exact='SS3').count()
    myfilter = StudentsFilter(request.GET, queryset= posts)
    posts=myfilter.qs
    counter = posts.count()
    context = {
        'posts':posts,
        'counter':counter,
        'jss1':jss1,
        'jss2':jss2,
        'jss3':jss3,
        'ss1':ss1,
        'ss2':ss2,
        'ss3':ss3,
        'myfilter':myfilter
    }
    return render(request, 'studentsms/index.html', context)

# add records
def add_students(request):
    if request.method == 'POST':
        form = studentsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentsms:add')
    
    form = studentsform()
    context= {
         'form':form
     }
    return render(request, 'studentsms/add.html', context)


def update_students(request,pk):
    id = students_reg.objects.get(pk=pk)
    form = studentsform(instance = id)
    if request.method == 'POST':
        form = studentsform(request.POST, instance = id)
        if form.is_valid():
            form.save()
            return redirect('studentsms:index')
    
    #form = studentsform()
    context= {
         'form':form
     }
    return render(request, 'studentsms/update.html', context)

def delete_students(request,pk):
    item = students_reg.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('studentsms:index')

    context= {
         'item':item
     }
    return render(request, 'studentsms/delete.html', context)

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def myview(request):
    posts = students_reg.objects.order_by('-created_date')
    context={
        'posts':posts
    }
    template_path = 'studentsms/pdf_filter.html'
    context = {'myvar': posts}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# download pdf all view
def pdf_all_view(request):
    posts = students_reg.objects.order_by('-created_date')
    counter = posts.count()
    myfilter = StudentsFilter(request.GET, queryset= posts)
    template_path = 'studentsms/pdf_all.html'
    context = {
        'posts':posts,
        'counter':counter,
        'myfilter':myfilter
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# download pdf id view
def pdf_id_view(request, *args, **kwarks):
    post = students_reg.objects.order_by('-created_date')
    pk = kwarks.get('pk')
    posts = get_list_or_404(students_reg, pk= pk)
    
    counter = post.count()
    template_path = 'studentsms/pdf_id.html'
    context = {
        'posts': posts,
        'counter':counter
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
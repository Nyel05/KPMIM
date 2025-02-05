from django.shortcuts import render
from Registration.models import Course
from Registration.models import Mentor
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    context= {
        'fathername': 'Abdullah'
    }
    return render (request,"index.html",context)

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data=Course(code=c_code, description=c_desc)
        data.save()
        allcourse = Course.objects.all().values()
        dict ={
            'message':'Data Save',
            'allcourse' : allcourse,
        }
    else:
        allcourse = Course.objects.all().values()
        dict = {
            'message':'Unsuccess',
            'allcourse' : allcourse,
        }
    return render(request,'course.html',dict)

def mentor(request):
    if request.method == 'POST':
        m_cd = request.POST['MID']  # Match the name in the form
        m_name = request.POST['MNAME']
        m_email = request.POST['MEMAIL']
        data = Mentor(mentorCd=m_cd, mentorName=m_name, mentorEmail=m_email)
        data.save()
        allmentor = Mentor.objects.all().values()
        dict = {
            'message': 'Data Save',
            'allmentor' : allmentor,
        }
    else:
        allmentor = Mentor.objects.all().values()
        dict = {
            'message': '',
            'allmentor' : allmentor,
        }
    return render(request, 'mentor.html', dict)

def search(request):
    if request.method == 'GET':
        c_code = request.GET.get('code')  # Get the 'code' input from the form

        if c_code:
            # Perform a case-insensitive search
            data = Course.objects.filter(code__iexact=c_code)
        else:
            data = None  # Handle the case where no code is provided

        # Pass data and error message to the template
        context = {
            'data': data,
            'message': "No data found." if not data else ""
        }
        return render(request, "search.html", context)

    # Render the search page with an initial message
    return render(request, "search.html", {"data": None, "message": "Enter a course code to search."})


def searchs(request):
    if request.method == 'GET':
        c_code = request.GET.get('mentorCd')  # Get the input from the form

        if c_code:
            # Adjust the filter to match your database field
            data = Mentor.objects.filter(mentorCd__iexact=c_code)  # Case-insensitive matching
        else:
            data = None

        # Pass data to the template
        context = {
            'data': data,
            'message': "No data found." if not data else ""
        }

        return render(request, "searchs.html", context)

    return render(request, "searchs.html", {"data": None, "message": "Enter a mentor code to search."})

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data' :data
    }
    return render (request , "update_course.html" , dict)

def save_update_course(request, code) :
    c_desc= request.POST['description']
    data=Course.objects.get(code=code)
    data.description = c_desc
    data.save()

    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code) :
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))






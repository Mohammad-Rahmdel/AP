from django.shortcuts import render
from portal.models import Course,AllCourses
from portal.forms import add_course_form, enroll_course_form

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# def index(request):
#     return user_login(request)

def st_cources(request):
    course_list = Course.objects.order_by('Id')
    id_dict = {'courses_records':course_list}
    return render(request,'portal/st_courses.html',context=id_dict)

def edit_info(request):
    return render(request,'portal/edit_info.html')

def home(request):
    return render(request,'portal/home.html')

def change_pw(request):
    return render(request,'portal/change_pw.html')

def register(request):
    form = enroll_course_form()
    all_course_list = AllCourses.objects.order_by('Id')
    form = enroll_course_form()
    if request.method == "POST":
        form = enroll_course_form(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            enrolled_course = AllCourses.objects.filter(Id=id).values()[0]
            temp = Course.objects.get_or_create(cName=enrolled_course['Name'],
                                            day=enrolled_course['Day'],
                                            Id=enrolled_course['Id'],
                                            time=enrolled_course['Time'])[0]
            temp.save()
            # print("id:"+str(enrolled_course))
    #         #form.save(commit=True)
            return st_cources(request)
        else:
            print('Error Form Invalid')
    return render(request,'portal/register.html',{'form':form,'all_courses_records':all_course_list})

def add_course(request):
    form = add_course_form()
    if request.method == "POST":
        form = add_course_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('Error Form Invalid')
    return render(request,'portal/add_course.html',{'form':form})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return home(request)
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'portal/login.html', {})

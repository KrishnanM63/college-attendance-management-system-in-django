from django.shortcuts import render,redirect
from django.contrib import messages
from attendance.forms import login_frm, register_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Add_students, MarkAttendance

def login_pg(request):
    form = login_frm()
    if request.method == "POST":
        form = login_frm(request.POST)
        form.is_valid()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        person = form.cleaned_data['login_as']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['role'] = person
            messages.success(request,"Login Successfully")
            if person == 'admin':
                return redirect("dashbort")
            else:
                return redirect("view")
    return render(request,"login.html",{'form':form})

def register_pg(request):
    form = register_form()
    if request.method == "POST":
        form = register_form(request.POST)
       
        if form.is_valid():
            login_as = request.POST.get('login_as')
            user =form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,"Register Successfully")
    
            return redirect("login_page")
          
        else:
            return render(request,"register.html",{'form':form})
                
            
            
    return render(request,"register.html")
def dashbor_pd(request):
    students = Add_students.objects.all()
    Total_stds = students.count()
    
   
    student_data = []

    for student in students:
        total = MarkAttendance.objects.filter(student=student).count()
        present = MarkAttendance.objects.filter(student=student, status='Present').count()
        
        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0
        
    return render(request,"dashbort.html",{'Total_stds':Total_stds,'percentage':percentage})

def view_attendance(request):
    roll_num = request.GET.get('roll_num')
    date = request.GET.get('date')
    attendance_records = MarkAttendance.objects.select_related('student').all().order_by('-date')
    if roll_num:
        attendance_records = attendance_records.filter(student__roll_num=roll_num)

    # Filter by Date
    if date:
        attendance_records = attendance_records.filter(date=date)
        
    return render(request,"view-attendance.html",{'records':attendance_records})
def add_students(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_num= request.POST.get('roll_num')
        email = request.POST.get('email')
        department = request.POST.get('department')
        year = request.POST.get('year')
        
        Add_students.objects.create(
            name=name,
            roll_num=roll_num,
            email=email,
            department=department,
            year=year
        )
        messages.success(request,"Student deatails add successfully!")
        return redirect("add")
    return render(request,"add_student.html")

def mark_the_attendance(request):
    students = Add_students.objects.all()

    if request.method == "POST":
        for student in students:
            status = request.POST.get(f'status_{student.id}')
            if status:
                MarkAttendance.objects.create(
                    student=student,  # pass actual object
                    status=status
                )
        messages.success(request, "Attendance marked successfully!")
        return redirect("mark")

    return render(request, "make_attendance.html", {"students": students})

def studen_list(request):
    return render(request,"")
def logout_pg(request):
    logout(request)
    return redirect("registerpage")
def report_pg(request):
    attendance_records = MarkAttendance.objects.select_related('student').all().order_by('-date')
    
    return render(request,"report.html",{'records':attendance_records})
def home(request):
    return render(request,"home.html")

   
   
        
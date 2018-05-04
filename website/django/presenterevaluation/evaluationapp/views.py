from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import AppAdminLoginForms, RegisterStudentForms, ProfessorLoginForms, RegisterProfessorForms, StudentLoginForms
from . models import AppAdmin, AppAdminLog, Professor, ProfessorVerify, Student, StudentLog, Presenter
from django.utils import timezone

# user_ref is used to show the username at home page
user_exists = False
user_ref = ''
user_log_obj = ''



def del_session(request):
    global user_exists, user_ref, user_log_obj
    user_exists = False
    user_ref = ''
    user_log_obj = ''

    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse('Session deleted...')

def logout_appadmin(request):
    try:
        user_log_obj.last_logged_out=timezone.now()
        user_log_obj.save()
    except AppAdmin.DoesNotExist:
        print('Error occurred while trying to log the logout')
    del_session(request)
    return redirect('index')

def validate_appadmin_login(request):
    global user_exists, user_ref, user_log_obj

    try:
        user = AppAdmin.objects.get(username=request.POST['username'])
        if user.password == request.POST['password']:
            print('password matched...')
            user_exists = True
            user_ref = request.POST['username']
            request.session['user_id'] = user.id
            user_log_obj = user.appadminlog_set.create(last_logged_in=timezone.now())
            return True
        else:
            print('password does not match....')
            del_session(request)
            return False
    except AppAdmin.DoesNotExist:
        print('value does not exist in table...')
        del_session(request)
        return False

def logout_professor(request):
    try:
        user_log_obj.last_logged_out=timezone.now()
        user_log_obj.save()
    except Professor.DoesNotExist:
        print('Error occurred while trying to log the logout')
    del_session(request)
    return redirect('professorlogin')

def validate_professor_login(request):
    global user_exists, user_ref, user_log_obj

    try:
        user = Professor.objects.get(username=request.POST['username'])
        if user.password == request.POST['password']:
            print('password matched...')
            user_exists = True
            user_ref = request.POST['username']
            request.session['user_id'] = user.id
            user_log_obj = user.professorlog_set.create(last_logged_in=timezone.now())
            return True
        else:
            print('password does not match....')
            del_session(request)
            return False
    except Professor.DoesNotExist:
        print('value does not exist in table...')
        del_session(request)
        return False

def logout_student(request):
    try:
        user_log_obj.last_logged_out=timezone.now()
        user_log_obj.save()
    except Student.DoesNotExist:
        print('Error occurred while trying to log the logout')
    del_session(request)
    return redirect('studentlogin')

def validate_student_login(request):
    global user_exists, user_ref, user_log_obj

    try:
        user = Student.objects.get(username=request.POST['username'])
        if user.password == request.POST['password']:
            print('password matched...')
            user_exists = True
            user_ref = request.POST['username']
            request.session['user_id'] = user.id
            user_log_obj = user.studentlog_set.create(last_logged_in=timezone.now())
            return True
        else:
            print('password does not match....')
            del_session(request)
            return False
    except Student.DoesNotExist:
        print('value does not exist in table...')
        del_session(request)
        return False


def appadminhome(request):
    if user_exists:
        if request.method == 'POST':
            return render(request, 'evaluationapp/appadminhome.html')
        else:
            return render(request, 'evaluationapp/appadminhome.html')
    else:
        return HttpResponse('Login again using the link: \'http://127.0.0.1:8000/appadmin/\' ')

def appadmin(request):
    del_session(request)
    app_admin_login_form = AppAdminLoginForms()

    if request.method == 'POST':
        if app_admin_login_form.is_valid:
            if validate_appadmin_login(request):
                return render(request, 'evaluationapp/appadminhome.html')
            else:
                context = {'appAdminLoginForms' : app_admin_login_form, 'message' : 'Username and Password did not match'}
                return render(request, 'evaluationapp/index.html', context)
    else:
        context = {'appAdminLoginForms' : app_admin_login_form}
        return render(request, 'evaluationapp/index.html', context)


def professorlogin(request):
    # just for safety
    del_session(request)
    professor_login_form = ProfessorLoginForms()

    if request.method == 'POST':
        if professor_login_form.is_valid:
            if validate_professor_login(request):
                return render(request, 'evaluationapp/professorhome.html')
            else:
                context = {'professorLoginForm' : professor_login_form, 'message' : 'Username and Password did not match'}
                return render(request, 'evaluationapp/professorlogin.html', context)
    else:
        context = {'professorLoginForm' : professor_login_form}
        return render(request, 'evaluationapp/professorlogin.html', context)

def professorhome(request):
    if user_exists:
        if request.method == 'POST':
            return render(request, 'evaluationapp/professorhome.html')
        else:
            return render(request, 'evaluationapp/professorhome.html')
    else:
        return HttpResponse('Login again using the link: \'http://127.0.0.1:8000/professor/\' ')

def reviewevaluation(request):
    if user_exists:
        if request.method == 'POST':
            return render(request, 'evaluationapp/reviewevaluation.html')
        else:
            return render(request, 'evaluationapp/reviewevaluation.html')
    else:
        return HttpResponse('Login again using the link: \'http://127.0.0.1:8000/professor/\' ')


def registerprofessor(request):
    professor_login_form = ProfessorLoginForms()

    if request.method == 'POST':
        if professor_login_form.is_valid:
            context = {'professorLoginForm' : professor_login_form}
            return  render(request, 'evaluationapp/registerprofessor.html', context)
    else:
        context = {'professorLoginForm': professor_login_form}
        return render(request, 'evaluationapp/registerprofessor.html', context)

def studentlogin(request):
    # just for safety
    del_session(request)
    studnet_login_form = StudentLoginForms()

    if request.method == 'POST':
        if studnet_login_form.is_valid:
            if validate_student_login(request):
                return render(request, 'evaluationapp/studenthome.html')
            else:
                context = {'studentLoginForm' : studnet_login_form, 'message' : 'Username and Password did not match'}
                return render(request, 'evaluationapp/studentlogin.html', context)
    else:
        context = {'studentLoginForm' : studnet_login_form}
        return render(request, 'evaluationapp/studentlogin.html', context)

def studenthome(request):
    if user_exists:
        if request.method == 'POST':
            return render(request, 'evaluationapp/studenthome.html')
        else:
            return render(request, 'evaluationapp/studenthome.html')
    else:
        return HttpResponse('Login again using the link: \'http://127.0.0.1:8000/professor/\' ')


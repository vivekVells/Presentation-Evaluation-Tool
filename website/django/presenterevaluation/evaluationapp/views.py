from django.shortcuts import render
from . forms import AppAdminLoginForms, StudentLoginForms, ProfessorLoginForms

def appadmin(request):
    app_admin_login_form = AppAdminLoginForms()

    if request.method == 'POST':
        context = {'appAdminLoginForms' : app_admin_login_form, 'message' : 'Username and Password did not match'}
        return render(request, 'evaluationapp/index.html', context)
    else:
        context = {'appAdminLoginForms' : app_admin_login_form}
        return render(request, 'evaluationapp/index.html', context)

def student(request):
    pass

def professor(request):
    pass


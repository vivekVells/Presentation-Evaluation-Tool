from django import forms

# App Admin Login Form
class AppAdminLoginForms(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


# Professor Login Form
class ProfessorLoginForms(forms.Form):
    mailId = forms.CharField(max_length=30,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mail ID'}))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    recovery_answer = forms.CharField(max_length=30,
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control', 'placeholder': 'Recovery Answer'}))
    recovery_email = forms.CharField(max_length=30,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Recovery Email'}))
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    middle_name = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    collegeName = forms.CharField(max_length=30,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': 'College Name'}))
    department = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
    phone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))


# Student Login Form
class StudentLoginForms(forms.Form):
    mailId = forms.CharField(max_length=30,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mail ID'}))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    recovery_answer = forms.CharField(max_length=30,
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control', 'placeholder': 'Recovery Answer'}))
    recovery_email = forms.CharField(max_length=30,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Recovery Email'}))
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    middle_name = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    collegeName = forms.CharField(max_length=30,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': 'College Name'}))
    department = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
    phone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))


# CourseForm
class CourseForms(forms.Form):
    course_name = forms.CharField(max_length=500,
                                 widget=forms.TextInput(attrs={'placeholder' : 'CourseName'}))


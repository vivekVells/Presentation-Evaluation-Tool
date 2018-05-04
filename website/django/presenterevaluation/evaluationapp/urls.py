from django.urls import path
from . views import appadmin, appadminhome, \
    professorlogin, professorhome, \
    studentlogin, studenthome, reviewmypresentation, evaluatepresentation, redirectoevaluate, \
    registerprofessor, logout_appadmin, logout_professor, logout_student

urlpatterns = [
    path('', appadmin, name='appadmin'),
    path('appadmin', appadmin, name='appadmin'),
    path('appadminhome', appadminhome, name='appadminhome'),

    path('studentlogin', studentlogin, name='studentlogin'),
    path('studenthome', studenthome, name='studenthome'),

    path('professorlogin', professorlogin, name='professorlogin'),
    path('professorhome', professorhome, name='professorhome'),

    path('evaluatepresentation', evaluatepresentation, name='evaluatepresentation'),
    path('reviewmypresentation', reviewmypresentation, name='reviewmypresentation'),
    path('redirectoevaluate', redirectoevaluate, name='redirectoevaluate'),

    path('registerprofessor', registerprofessor, name='registerprofessor'),

    path('logoutappadmin', logout_appadmin, name='logoutappadmin'),
    path('logoutprofessor', logout_professor, name='logoutprofessor'),
    path('logoutstudent', logout_student, name='logoutstudent'),
]
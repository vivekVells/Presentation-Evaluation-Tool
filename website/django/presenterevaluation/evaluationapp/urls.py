from django.urls import path
from . views import appadmin, student, professor

urlpatterns = [
    path('', appadmin, name='appadmin'),
    path('student', student, name='student'),
    path('professor', professor, name='professor'),
]
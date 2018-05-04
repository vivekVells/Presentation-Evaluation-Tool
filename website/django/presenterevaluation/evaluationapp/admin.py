from django.contrib import admin
from . models import AppAdmin, AppAdminLog, Professor, \
    ProfessorVerify, ProfessorLog, Student, StudentLog, Presenter, PresenterNew

admin.site.register(AppAdmin)
admin.site.register(AppAdminLog)
admin.site.register(Professor)
admin.site.register(ProfessorVerify)
admin.site.register(ProfessorLog)
admin.site.register(Student)
admin.site.register(StudentLog)
admin.site.register(Presenter)
admin.site.register(PresenterNew)

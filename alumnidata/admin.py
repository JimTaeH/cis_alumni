from django.contrib import admin
from .models import (Profile, academicadmin, assistantDean, alumnidata, 
                    fieldstudy, job, education, success,
                    alumniList, adminList, assistantDeanList)

# Register your models here.
admin.site.register(Profile)
admin.site.register(alumnidata)
admin.site.register(academicadmin)
admin.site.register(assistantDean)
admin.site.register(fieldstudy)
admin.site.register(job)
admin.site.register(education)
admin.site.register(success)
admin.site.register(alumniList)
admin.site.register(adminList)
admin.site.register(assistantDeanList)
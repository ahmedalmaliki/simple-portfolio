from django.contrib import admin
from .models import User, Experience, Languages, Projects, Skills

class UserAdmin(admin.ModelAdmin):
    list_display = ['Fullname', 'Profile',  'Address', 'Phone', 'Email', 'Website']

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['startYear' , 'endYear' , 'describe']

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['language']

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['projectName', 'projectLink', 'projectDescription']

class SkillsAdmin(admin.ModelAdmin):
    list_display = ['skillName']



# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Skills, SkillsAdmin)

from django.contrib import admin
from .models import Project, Work, Education, Skills, Hobbies,Contact, IndexBody

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title','description','image','url']
    search_fields=['title','descriptin']
    list_filter=['title','description']
    list_per_page= 10

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','birth_date','phone','email','weblink']
    search_fields=['name']
    list_filter=['email']
    list_per_page=5

@admin.register(Hobbies)
class HobbiesAdmin(admin.ModelAdmin):
    list_display=['name','description','image','url']
    search_fields=['name']
    list_filter=['name']
    list_per_page= 10

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display=['title','Work_description', 'Institution', 'start_date', 'end_date']
    search_fields=['title', 'Institution']
    list_filter=['title', 'Institution']
    list_per_page=10

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display=['certification','school','start_date', 'end_date']
    search_fields=['certification','school']
    list_filter=['certification','school']
    list_per_page=10

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display=['language','level']
    search_fields=['language']
    list_filter=['language']
    list_per_page=10

@admin.register(IndexBody)
class IndexBodyAdmin(admin.ModelAdmin):
    list_display=['icon', 'ContentName', 'ContentDesc']
    search_fields=['ContentName']
    list_filter=['ContentName']
    list_per_page=10

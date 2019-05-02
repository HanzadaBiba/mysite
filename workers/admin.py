from django.contrib import admin

# Register your models here.
from django.contrib import admin
from workers.models import Units,Block,Departaments,Departament_block,Position,City,Workers
# Register your models here.
a=[Units,Block,Departaments,Departament_block,Position,City,Workers]
class UnitsAdmin(admin.ModelAdmin):
    list_display = ['name']

    prepopulated_fields = {'slug':['name']}
class BlockAdmin(admin.ModelAdmin):
    list_display = ['name','units']
    prepopulated_fields = {'slug': ['name']}
class DepartamentsAdmin(admin.ModelAdmin):
    list_display =['name','block','units']

    prepopulated_fields = {'slug':['name']}
class Departament_block_admin(admin.ModelAdmin):
    list_display = ['name','deps']

    prepopulated_fields = {'slug':['name']}
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']

    prepopulated_fields = {'slug':['name']}
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

    prepopulated_fields = {'slug':['name']}
class WorkersAdmin(admin.ModelAdmin):
    list_display = ['firstname','secondname','lastname','deps','deps_block','position','room','ip_number','city','mobile_phone']

    prepopulated_fields = {'slug':['firstname']}
admin_klass=[UnitsAdmin,BlockAdmin,DepartamentsAdmin,Departament_block_admin,PositionAdmin,CityAdmin,WorkersAdmin]
for i,b in zip(a,admin_klass):
    admin.site.register(i,b)
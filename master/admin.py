# 
#   file: admin.py
#	author: andromeda
#   desc: Models registration on administrator page
#
from django.contrib 			import admin
from .models 					import tbProjekte, tbComponent
from tinymce.widgets 			import TinyMCE
from django.db 					import models


# Register your models here.
class ProjekteAdmin(admin.ModelAdmin):

	fieldsets = [
		("Project Title/Author/Date", {'fields': ["projTitle", "projAuthor", "projCreated"]}),
		("Project Description", {"fields": ["projDesc"]})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()},
	}

class ComponentAdmin(admin.ModelAdmin):

	fieldsets = [
		("Component Name", {'fields': ["compName"]}),
		("Component Package & Distributor", {'fields': ["compPackage", "compDist"]}),
		("Component Description", {"fields": ["compDesc"]}),
		("Component Part Number", {'fields': ["compPartNum"]}),
		("Total", {"fields": ["compTotal"]})
	]
	
	search_fields = ('compName', 'compPackage',
					 'compDist', 'compDesc',
					 'compPartNum')


admin.site.register(tbProjekte,ProjekteAdmin)
admin.site.register(tbComponent,ComponentAdmin)
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from miniproject.settings import BASE_DIR

class IDE(LoginRequiredMixin, View):
	'''
		Class comments
	'''
	login_url = '/admin/login/'
	redirect_field_name = 'next'
	html_template_file = 'mini/IDE.html'
	# model = model_name
	# form = form_name

	def get(self, request):
		# get method
		IDE_DEFAULT_content = "<h2><table><tr><td><p></td><td><p>Rich Text Editor is the industry-leading online html editor. It enables content contributors easily create and publish HTML anywhere: on the desktop and on mobile.</p></td></tr><tr><td><p></td><td><p>Rich Text Editor toolbar is completely configurable and it is also effortless to implement. You just need a couple lines of code to add this editor to web applications.</p></td></tr></table>"
		print(IDE_DEFAULT_content)
		return render(request, self.html_template_file, locals())

	def post(self, request):
		 
	 	app = request.POST['app_name'] + '\\templates\\' + request.POST['app_name'] 
	 	file = request.POST['file_name'] + '.html'
	 	content = request.POST['html_code']
	 	app_path = os.path.join(BASE_DIR, app)
	 	file_path = os.path.join(app_path, file)
	 	print(app,file,BASE_DIR, file_path)
	 	try:
	 		with open(file_path, 'w') as fp:
	 			fp.write(content)
	 			fp.close()
	 	except:
	 		message = 'Something went wrong! Check all file names are correct.'
	 	return render(request, self.html_template_file, context={'IDE_DEFAULT_content':content, 'message':message})

class Dashboard(LoginRequiredMixin, View):
	'''
		Class comments
	'''
	login_url = '/admin/login/'
	redirect_field_name = 'next'
	html_template_file = 'mini/dashboard.html'
	# model = model_name
	# form = form_name

	def get(self, request):
		# get method
		return render(request, self.html_template_file, locals())

	def post(self, request):
		# Post method
		return 

class Preview(LoginRequiredMixin, View):
	'''
		To preview the files that are in creation.
	'''
	login_url = '/admin/login/'
	redirect_field_name = '/mini/ide/'
	html_template_file = 'mini/preview_file.html'
	# model = model_name
	# form = form_name

	def get(self, request, fname = None):
		# get method
		return render(request, self.html_template_file, locals())

	def post(self, request):
		# Post method
		return 


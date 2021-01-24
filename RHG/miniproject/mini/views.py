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
	
	context = {}
	context['page_name'] = 'IDE'

	def get(self, request):
		IDE_DEFAULT_content = "<h2><table><tr><td><p></td><td><p>Rich Text Editor is the industry-leading online html editor. It enables content contributors easily create and publish HTML anywhere: on the desktop and on mobile.</p></td></tr><tr><td><p></td><td><p>Rich Text Editor toolbar is completely configurable and it is also effortless to implement. You just need a couple lines of code to add this editor to web applications.</p></td></tr></table>"
		print(IDE_DEFAULT_content)
		return render(request, self.html_template_file, locals())

	def post(self, request):
		app_name = request.POST['app_name']
		file_name = request.POST['file_name']
		content = request.POST['html_code']
		self.context['IDE_DEFAULT_content'] = content
		app = app_name + '\\templates\\' + app_name
		file = file_name + '.html'
		local_path = os.path.join(app, file)
		file_path = os.path.join(BASE_DIR, local_path)

		try:
			with open(file_path, 'w') as fp:
				fp.write(content)
				fp.close()
				message = 'File saved : ' + file_path
		except:
			message = 'Something went wrong! Check all file names are correct.'

		self.context['message'] = message
		return render(request, self.html_template_file, context=self.context)

class Dashboard(LoginRequiredMixin, View):
	'''
		Class comments
	'''

	login_url = '/admin/login/'
	redirect_field_name = 'next'
	html_template_file = 'mini/dashboard.html'

	# model = model_name
	# form = form_name

	context = {}
	context['page_name'] = 'Dashboard'
	file_data = []
	
	def get(self, request):
		self.getListOfFiles('')
		self.context['files'] =  self.file_data
		return render(request, self.html_template_file, context = self.context)

	def post(self, request):
		# Post method
		return

	def getListOfFiles(self, Name):
		dirName = os.path.join(BASE_DIR, Name)
		l = len(BASE_DIR.split('\\'))
		print(os.walk(dirName, topdown=False))
		for root, dirs, files in os.walk(dirName, topdown=False):
			root = '\\'.join(root.split('\\')[l:])

			self.file_data.append({'root': root,'dirs': dirs, 'files': files})
			


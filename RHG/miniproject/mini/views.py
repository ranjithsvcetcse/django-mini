from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from miniproject.settings import BASE_DIR
from django.contrib.auth import logout
import os

class IDE(LoginRequiredMixin, View):
	'''
		The UI powered editing environment. Admin login is mandatory to access this page.
		User may need to login with Admin login credentials to continue to this page.
	'''
	login_url = '/admin/login/'
	redirect_field_name = 'next'
	html_template_file = 'mini/IDE.html'
	# model = model_name
	# form = form_name
	
	context = {}
	context['page_name'] = 'IDE'

	def get(self, request, file = 'default.html'):
		# print(file)
		try:
			base_template_path = Dashboard.template_path
			formdata = {'app_name': 'mini', 'file_name': file}
			self.context['formdata'] = formdata
			# print('succes')
		except:
			base_template_path = os.path.join(BASE_DIR, 'mini\\templates\\mini')

		file_abs_path = os.path.join(base_template_path, file)
		# print(file_abs_path)

		with open(file_abs_path, 'r') as f:
			l=f.read()
			# print(l)
			self.context['IDE_DEFAULT_content'] = self.remove_new_lines(l)
			f.close()
		# print(self.context['IDE_DEFAULT_content'])

		return render(request, self.html_template_file, context = self.context)

	def post(self, request):

		app_name = request.POST['app_name']
		file_name = request.POST['file_name']
		content = request.POST['html_code']
		formdata = {'app_name': app_name, 'file_name': file_name}
		self.context['formdata'] = formdata

		app = app_name + '\\templates\\' + app_name
		file = file_name + '.html'
		local_path = os.path.join(app, file)
		file_path = os.path.join(BASE_DIR, local_path)

		# print(app,file,BASE_DIR, file_path)
		# print(content, request.POST,app_name)

		try:
			with open(file_path, 'w') as fp:
				# code = '<!DOCTYPE html><html><head><title></title></head><body>' + content + '</body></html>'
				# code = self.add_newline(content)
				fp.write(content)
				fp.close()
				message = 'File saved : ' + file_path
		except:
			message = 'Something went wrong! Check all file names are correct.'
		
		self.context['IDE_DEFAULT_content'] = self.escape_chars(content, ["'"])
		self.context['message'] = message

		return render(request, self.html_template_file, context=self.context)

	def escape_chars(self, code, charlist):
		temp, esc = '', '\\'
		for _ in code:
			temp += esc + _ if _ in charlist else _
		return temp

	def add_newline(self, code):
		temp, nl = '', '\n'
		for _ in code:
			temp += nl + _ if _ == '<' else _
		return temp

	def remove_new_lines(self, code):
		temp, nl = '', '<br>'
		for _ in code:
			temp += nl if _ == '\n' else _
		return temp

	

class Dashboard(LoginRequiredMixin, View):
	'''
		Dashboard contains a list of html files in the app's template folder.
		The app name is required as input.
	'''
	login_url = '/admin/login/'
	redirect_field_name = 'next'
	html_template_file = 'mini/dashboard.html'
	# model = model_name
	# form = form_name
	context = {}
	context['page_name'] = 'Dashboard'
	# file_data = ['']
	
	def get(self, request):
		
		# self.getListOfFiles('')
		# self.context['files'] =  self.file_data
		return render(request, self.html_template_file, context = self.context)

	def post(self, request):
		app_name = request.POST['app_name']
		# print(app_name+'\\templates')
		self.template_path = os.path.join(BASE_DIR, app_name+'\\templates\\'+app_name)
		pre_defined_files = ['default.html' ,'dashboard.html', 'IDE.html', 'layout.html', 'header.html', 'footer.html']
		try:
			all_files, error =  self.getListOfFiles(app_name+'\\templates\\'+app_name)
			# print(all_files[0]['files'])
			# print(all_files)
			# print(pre_defined_files)
			# a=[i if i not in pre_defined_files else None for i in all_files[0]['files']]
			a=[]
			for _ in all_files[0]['files']:
				if _ not in pre_defined_files:
					a.append(_)
			all_files[0]['files'] = a
			self.context['files'] = all_files

		except:
			error = 'Invalid app : Cannot find ' + app_name 
		# print(self.file_data)
		self.context['error'] = error
		error=''
		return render(request, self.html_template_file, context = self.context) 

	def getListOfFiles(self, Name):
		dirName = os.path.join(BASE_DIR, Name)
		# print(dirName)
		l = len(BASE_DIR.split('\\'))
		# print(os.walk(dirName, topdown=False))
		file_data = []
		for root, dirs, files in os.walk(dirName, topdown = False):
			root = '\\'.join(root.split('\\')[l:])
			file_data.append({'root': root,'dirs': dirs, 'files': files})
			# print(root,dirs,files)
		if len(file_data) <= 0:
			error = Name + ' is empty.'
		else:
			error = 'No error'
		# print(file_data)
		return file_data, error

def logout_view(request):
    logout(request)
    return redirect('mini_IDE')


.. README.rst
Mini
=====

Mini is a reusable Django app to convert text to HTML and apply styles. It saves code directly to the django's template folders. HTML code can also be downloaded as a seperate file.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "mini" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'mini',
    ]

2. Include the admin & mini URLconf in your project urls.py like this::

    path('admin/', admin.site.urls),
    path('mini/', include('mini.urls')),

3. Run ``python manage.py migrate`` to create the mini models.

4. Use ``python manage.py createsuperuser`` to create Super User.

5. Start the development server and visit ``http://127.0.0.1:8000/mini/dashboard/`` or ``localhost:8000/mini/dashboard/`` to start using mini (you'll need the Admin app enabled and super user created).

6. Visit ``http://127.0.0.1:8000/mini/ide`` or simply ``localhost:8000/mini/ide/`` to start using the editor.
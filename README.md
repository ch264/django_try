# django
# django_try

This project is a test project to deploy to Pythonanywhere : www.pythonanywhere.com.

Here is a step-by-step guide on how to deploy to a Django-Python app on Pythonanywhere.

1. Create python anywhere account
2. Open bash console in pythonanywhere dashboard
3. ``git clone <your project>``` 

4. Create new environment and specify the python version your app is written in:
```mkvirtualenv --python=/usr/bin/python3.5 any_name```

5. Install Django in virtual environment: 
```pip install django```

6. Install the requirements that you need for your app. (Cd into your folder if needed)
```pip install -r requirements.txt```


7. Create a new App: go to the 'web' tab and add a new web app and select manual configuration and select the python version you are using (3.5).

8. Set virtual environment:
Pick the same name you used to create environment in bash (any_name)

9. Edit WSGI configuration file:
Click on the WSGI file and it opens in Pythonanywhere text editor.
You can remove any code that is not for your framework and comment-in any code you need for your framework (in this case Django).

10. Then modify the path to the path that your project is in: (go back to your bash, cd to your project and type: pwd to get the path)

11. then modify the settings module to the name of your Django app! 

12. Save and close

13. Click the reload button in your dashboard. Once reloaded open in browser and copy the url

14. Go to the 'Files' tab and find your 'settings.py' file and copy url in to ALLOWED HOSTS: ALLOWED_HOSTS = ["ch264.pythonanywhere.com"]

15. Add a static Root below STATIC: 
```STATIC_ROOT = '/home/ch264/django_try/mysite/static'```
Note: the new static folder has to be created at the same level as your manage.py file!

16. Go to bash console and run:
```python manage.py collectstatic```



17. Then change static file settings in your Pythonanywhere dashboard: 
Url: /static/
Directory: the one you supplied for the static root: /home/ch264/django_try/mysite/static

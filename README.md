# Django Commands and Workflow

```
django-admin startproject djangoUnchained
```

```
PgAdmin > New Server > localhost > username(Schultz)/password(GQ!)
If forget password... edit PostgreSQL\<version>\data\pg_hba.conf IPv4/6 method to trust
Login/Group Roles > Create > Role > User & Pass > superuser
Create Database with name and select user 

edit DATABASES in project/settings.py
edit INSTALLED_APPS in project/settings.py (add graphene_django)
Add a URL pattern for GraphQL in project/urls.py
```

```
py manage.py startapp core
```

```
add model item to core/models.py
add 'core' to project/settings.py INSTALLED_APPS
```

```
py manage.py makemigrations core
py manage.py migrate
py manage.py createsuperuser
```

```
create schema.py with required installed app and query
import schema to project/urls.py and add as arg to urlpatterns path

add something to views.py for the homepage
add this to urls.py with from core.views import home
set DEBUG = False in settings.py and add localhost to ALLOWED_HOSTS

views.py homepage looks shit so

cd core, mkdir templates, edit TEMPLATES in settings.py, add templates folder to dirs 
create html in templates dir
mkdir core/static
mkdir core/static/css
add styles.css
add {% load static %} to top of .html
link stylesheet to .html with     <link rel="stylesheet" href="{% static 'css/styles.css' %}">

add to settings.py STATICFILES_DIRS = [os.path.join(BASE_DIR, 'core/static'),]
add to settings.py STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
add to settings.py BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

add whitenoise to MIDDLEWARE to manage static files for debug = false along with STATICFILES_STORAGE
turn off DEBUG=TRUE in settings requires whitenoise to manage static files for deployment
```

```
py manage.py collectstatic
py manage.py runserver
```

With Django setup with the min requirements, setup React for the frontend

```
mkdir frontend
touch webpack.config.js and package.json to avoid 10 billion audit error caused with npx
copy public dir manually (pain in the ass but avoids 10 billion audit errors with react from npx)
```

```
npm init -y
npm install
npm run build
npm start
```

Integrate React with Django

```
Need CORS
add 'corsheaders' to INSTALLED_APPS and to MIDDLEWARE
add CORS_ALLOWED_ORIGINS for React URL
add proxy localhost:8000 to package.json
add GRAPHENE arg to settings.py to use schema from graphql
add "@apollo/client" and "graphql" to package.json dependencies
add an apollo import and wrapper to the app in index.js
build react app and move build folder to static folder in django
update urls.py to include build/index.html
update settings.py to include core/static/build to DIRS in TEMPLATES
```

Get data in DB and plot with GraphQL and visualise with recharts

```
add a class to core/models.py to define a new database table/fields
import class to schema to server on django api endpoint via graphene
?????
data goes into database (make script, import table class from model, loop through tuple data, model_class.objects.create(tuple_data_vars))
npm install recharts
import useQuery and recharts stuff to App.js
def var to query data from graphql using apollo
def func to useQuery(query_var) and return LineChart from recharts plotting the data, add as a div like a react component
add csrf_exempt() wrapper to GraphQLView in urls.py to bypass 403
```
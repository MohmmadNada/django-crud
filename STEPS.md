# django-crud
### setup 
run in your terminal :
1. `poetry new django_models`
2. `cd django_models`
3. `poetry add --dev black`
4. `touch django_models.py`
5. ` mv README.rst README.md`
### Github : 
 1. create EMPTY repository django-models on Github. Do NOT initialize with README, license or gitignore.
### connect Github with your local machine:
 1. `echo "# django-models" >> README.md
 2. git init
 3. git add README.md
 4. git commit -m "first commit"
 5. git branch -M main
 6. git remote add origin https://github.com/MohmmadNada/django-models.git
 7. git push -u origin main`
### Run in ypur terminal :
 1. `poetry add django`
 2. `poetry shell`

### create snacks_crud_project project:
 1. `django-admin startproject snacks_crud_project .` 
          1. this command must write once
          2. (.) in the last very important, its means here 
 2. `python manage.py migrate`
 3. `python  manage.py runserver`

### create snacks app
1. `python manage.py startapp snacks`

### Add snacks app to project
##### Setting section
 1. go to snacks_crud_project =>  settings => INSTALLED_APPS => add last items ` 'snacks.apps.SnacksConfig' `
 2. go to snacks_crud_project =>  settings => `import os` => modife to `'DIRS': [os.path.join(BASE_DIR, 'templates')],`
### create Snack model
 * make sure it extends from proper base class
 * add title field as a CharField with maximum length of 64 characters.
 * add purchaser 
 * add description TextField
 * Register model with admin
 
 1. go to snacks => models.py => add class and import 
##### Urls section 
 1. go to snacks_crud_project => urls.py => import `from django.urls import include`
 2. go to snacks_crud_project => urls.py => `path('/',include('snacks.urls')),`
 3. go to snacks => create urls.py file => `path('/',include('snacks.urls')),`
 4. go to snacks => urls.py => import path and HomeView , add urlpatterns then path  
##### Views section 
 1. go to snacks => views.py => import TemplateView => Add class and template_name into model if needed
 2. add templates folder and add html file  

 
 2. run `python mange.py makemigrations`  
    > the command will scan the models and cerate model 
 3. check the snacks => migrations => will have  0001_initial.py file 
 4. run `python manage.py migrate` Applying the new file 
 5. run `python manage.py createsuperuser` enter data (name , email and password ) 
 6. Go to snacks => admin.py => import register and class = > Register your models Snack.
    1. `from django.contrib.admin.decorators import register`
    2. `from .models import Snack`
    3. `admin.site.register(Snack)`
 7. add data from browser 
    1. run `python mange.py runserver`
    2. open link in browser
    3. add /admin in url and enter data req
    4. Add a few snacks via Admin panel

### Views for Snacks App
Where to create these views?
1.  GO to app => views => create SnackListView
  * extend ListView
  * give a template of snack_list.html
  * associate Snack model
    * update url patterns for project
    * associated url path is an empty string
    * update snacks app urls
      * snacks =>url.py =>  ` path('', SnackListView.as_view(), name='home'),`
      * Don’t forget to use as_view()
  2.  add SnackDetailView
        * link snack_detail.html template => model=Snack 
          * associate Snack model 
    * update app urlpatterns to handle detail view
        * account for primary key in url 
          * `path('<int:pk>', SnackDetailView.as_view(), name='detail'),`
        * path would look like localhost:8000/1/ to get to snack with id of 1
    3. SnackCreateView , associated url path is create/
       1. app=> views.py 
          1. import  CreateView
          2. add template_name and model as needed
          3. add array as model name `fields=['title','purchaser','description']`
       2. app => url 
          1. import CreateView
          2. add path `path('create/',SnackCreateView.as_view(),name='create'),`
    4. Create SnackUpdateView 
        * associated url path is <int:pk>/update/
            1. app=> views.py 
            2. import  SnackUpdateView
            3. add template_name and model as needed
            4. add array as model name `fields=['title','purchaser','description']`
            5. app => urls =>import class and add path 
    5. Create SnackDeleteView
       * associated url path is <int:pk>/delete/
          1. app=> views.py 
          2. import  SnackUpdateView
          3. add template_name and model as needed
          4. add success_url , use reverse_lazy witht page name , that you want to go after delete 
          5.  app => urls =>import class and add path 

### Templates , from lab req

  1. Add templates folder in root of project (already done)
  2. register templates folder in project settings TEMPLATES section (already done)
  3. create base.html ancestor template
     1. add main html document
     2. use Django Templating Language to allow child templates to insert content
  4. create snack_list.html template
      * extend base template
      * use Django Templating Language to display each snack’s name
  5. view home page (aka snack_list) and confirm snacks showing properly
  6. create snack_detail.html template
      * template should extend base
      * content should display snack’s name, description and purchaser
  7. add link in snack_list template to related detail page for each snack
  8. Add a link back to Home (aka snack_list) page from detail page.

### CRUD part 
1. add list to html home 
2. add detail page content 
##### Create 
1. app => add path to create url [x]
2. app => views => import create and add class.
   1. template_name
   2. connect with model
   3. add html file extend from base html   
   4. add form , the form must reflect you model ```<form action="" method="POST">
    {{ form }}
    <input type="submit">
</form>```
    5. check from browser 
    6. the input depands in fields in view class SnackCreateView
    7. add {% csrf_token %}  in the form , more security
    8. from app => model => add get_absolute_url method 
    9. the new snack is added 

##### Update 
1. app => add path to create url [x]
2. app => views => import create and add class.
   1. template_name
   2. connect with model
   3. add html file extend from base html   
   4. add form , the form must reflect you model ```<form action="" method="POST">
    {{ form }}
    <input type="submit">
</form>```
    5. check from browser 
    6. the input depands in fields in view class SnackCreateView
    7. add {% csrf_token %}  in the form , more security
    8. done , updated
  * add update botton in detail page 
    * with link {% url 'update' snack.pk %}
    9. add delete button 
       1.  add class in views 
       2.  add path in url 
       3.  add `<input type="submit" value="Delete">`  
       4.  from view add `success_url=reverse_lazy('home')`


### Test Snack pages
> NOTE make sure test extends TestCase instead of SimpleTestCase used in previous class.
1. verify status code
2. verify correct template use
> use url name instead of hard coded path
    > 1. TIP: django.urls.reverse will help with that.
    > 2. We can’t easily test SnackDetailView just yet. its dynamic 
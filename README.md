# Just-Django-Tutorial

## SIGNALS

Signals consists of a sender and receiver
Used to listen for events
post_save and pre_save are used to send signals before or after data is saved in the database
post_save => Add logic after saving something to the database
pre_save=>Add logic before saving something to the database

## CRUD

CRUD stands for create-read-update-delete
all websites can be categorized under  CRUD
django.views.generic has the following  CRUD operation classes

1. TemplateView => Displaying a template
2. CreateView =>Creating a new object with a form
3. DeleteView=>Deleting
4. ListView=>showing a list
5. UpdateView=>updating

context passed thru a class view is reffered to as object_list
But we can customise it by this : context_object_name="leads"

## EMAIL CONTEXT that is passed to the email template

for user in self.get_users(email):
            user_email = getattr(user, email_field_name)
            context = {
                "email": user_email,
                "domain": domain,
                "site_name": site_name,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": token_generator.make_token(user),
                "protocol": "https" if use_https else "http",
                **(extra_email_context or {}),
            }

## CRISPY FORMS

pip install crispy-tailwind
pip install django-crispy-forms

CONFIGURATION
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

## ENVIRONMENT CONFIGURATION

1. install an environment package:
        $  pip install django-environ

2. Create a .env file and add the following configurations
DEBUG=on
SECRET_KEY=your-secret-key
DATABASE_URL=psql://user:un-githubbedpassword@127.0.0.1:8458/database
SQLITE_URL=sqlite:///my-local-sqlite.db
CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213
REDIS_URL=rediscache://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret

3. settings.py
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

Set the project base directory

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Take environment variables from .env file

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

False if not in os.environ because of casting above

DEBUG = env('DEBUG')

Raises Django's ImproperlyConfigured

exception if SECRET_KEY not in os.environ

SECRET_KEY = env('SECRET_KEY')

 Parse database connection url strings

like psql://user:pass@127.0.0.1:8458/db

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    #
    # The db() method is an alias for db_url().
    'default': env.db(),

    # read os.environ['SQLITE_URL']
    'extra': env.db_url(
        'SQLITE_URL',
        default='sqlite:////tmp/my-tmp-sqlite.db'
    )
}

CACHES = {
    # Read os.environ['CACHE_URL'] and raises
    # ImproperlyConfigured exception if not found.
    #
    # The cache() method is an alias for cache_url().
    'default': env.cache(),

    # read os.environ['REDIS_URL']
    'redis': env.cache_url('REDIS_URL')

## environment configuration

1. Take environment variables from .env file

READ_DOT_ENV_FILE = env.bool('READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    environ.Env.read_env()

## Freezing Requiremets

1. freezing:
        pip freeze > requirements.txt
2. Installing Requirements
    pip install -r requirements.txt

## POSTGRES DATABASE INSTALLATION AND CONFIGURATION

1. MACOS
    1. open the terminal
    2. brew update
    3. brew install postgresql
    4. brew services restart postgresql@14
    5. createuser -s postgres
    6. psql postgres postgres
    7. ALTER USER postgres WITH PASSWORD 'password';
    8. install pyAdmin 4 and use the user and password above to login

2. CREATING A USER USING THE VSCODE TERMINAL
    1. psql postgres postgres
    2. CREATE USER  djcrmuser WITH PASSWORD '7040';
    3. GRANT ALL PRIVILEGES ON DATABASE djcrm TO djcrmuser;
    4. exit psql shell \q

3. UNINSTALLING POSTGRESS
    1. brew uninstall postgresql
    2. cd Library and uninstall postgresql from there

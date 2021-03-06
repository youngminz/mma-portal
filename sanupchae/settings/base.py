import os

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

load_dotenv()


def get_env_variable(var_name, default=None):
    try:
        return os.environ[var_name]

    except KeyError:
        if default is None:
            error_msg = f"필수 환경 변수 {var_name}가 설정되지 않았습니다."
            raise ImproperlyConfigured(error_msg)

        return default


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = get_env_variable("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ['*']

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'rest_framework',
    'storages',
    'django_filters',
]

LOCAL_APPS = [
    'company',
    'notice',
    'users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'sanupchae.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../../templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sanupchae.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': get_env_variable("DATABASE_ENGINE"),
        'NAME': get_env_variable("DATABASE_NAME"),
        'USER': get_env_variable("DATABASE_USER"),
        'PASSWORD': get_env_variable("DATABASE_PASSWORD"),
        'HOST': get_env_variable("DATABASE_HOST"),
        'PORT': get_env_variable("DATABASE_PORT"),
        'OPTIONS': {
            'isolation_level': 'REPEATABLE READ',
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
}

LANGUAGE_CODE = 'ko'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False
STATIC_URL = '/static/'

BROKER_URL = get_env_variable("BROKER_URL")

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = get_env_variable('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'files/'
AWS_S3_REGION_NAME = 'ap-northeast-2'
AWS_QUERYSTRING_AUTH = False

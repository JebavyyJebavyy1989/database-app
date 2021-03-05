"""
Django settings for djangoproject project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "jsondataferret.apps.JsondataferretConfig",
    "indigo.apps.IndigoConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "indigo.middleware.TemplateContextMiddleware",
]

ROOT_URLCONF = "djangoproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djangoproject.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

LOGIN_REDIRECT_URL = "/app/"

# We disable MemoryFileUploadHandler - there is code in app that assumes all files are written to disk
FILE_UPLOAD_HANDLERS = ["django.core.files.uploadhandler.TemporaryFileUploadHandler"]

JSONDATAFERRET_SPREADSHEET_FORM_DATE_FORMAT = "%Y-%m-%d"


def load_guide_form_spec(filename):
    fn = os.path.join(
        BASE_DIR,
        "indigo",
        "spreadsheetform_guides",
        "cached_information",
        filename + ".guidespec.json",
    )
    with open(fn) as fp:
        return json.load(fp)


def load_json_schema(filename):
    fn = os.path.join(
        BASE_DIR,
        "indigo",
        "jsonschema",
        "cached_information",
        filename + ".compiled_jsonschema.json",
    )
    with open(fn) as fp:
        return json.load(fp)


def load_json_schema_fields(filename):
    fn = os.path.join(
        BASE_DIR,
        "indigo",
        "jsonschema",
        "cached_information",
        filename + ".fields.json",
    )
    with open(fn) as fp:
        return json.load(fp)


def load_json_schema_filter_keys(filename):
    fn = os.path.join(
        BASE_DIR,
        "indigo",
        "jsonschema",
        "cached_information",
        filename + ".filter_keys.json",
    )
    with open(fn) as fp:
        return json.load(fp)


JSONDATAFERRET_TYPE_INFORMATION = {
    "project": {
        "json_schema": load_json_schema("project.json"),
        "spreadsheet_form_guide": os.path.join(
            BASE_DIR, "indigo", "spreadsheetform_guides", "project_v012.xlsx",
        ),
        "spreadsheet_form_guide_spec": load_guide_form_spec("project_v012.xlsx"),
        "spreadsheet_form_guide_spec_versions": {
            7: load_guide_form_spec("project_v007.xlsx"),
            8: load_guide_form_spec("project_v008.xlsx"),
            9: load_guide_form_spec("project_v009.xlsx"),
            10: load_guide_form_spec("project_v010.xlsx"),
            11: load_guide_form_spec("project_v011.xlsx"),
            12: load_guide_form_spec("project_v012.xlsx"),
        },
        "fields": load_json_schema_fields("project.json"),
        "filter_keys": load_json_schema_filter_keys("project.json"),
    },
    "organisation": {
        "json_schema": load_json_schema("organisation.json"),
        "spreadsheet_form_guide": os.path.join(
            BASE_DIR, "indigo", "spreadsheetform_guides", "organisation_v004.xlsx",
        ),
        "spreadsheet_form_guide_spec": load_guide_form_spec("organisation_v004.xlsx"),
        "spreadsheet_form_guide_spec_versions": {
            2: load_guide_form_spec("organisation_v002.xlsx"),
            3: load_guide_form_spec("organisation_v003.xlsx"),
            4: load_guide_form_spec("organisation_v004.xlsx"),
        },
        "fields": load_json_schema_fields("organisation.json"),
    },
    "fund": {
        "json_schema": load_json_schema("fund.json"),
        "spreadsheet_form_guide": os.path.join(
            BASE_DIR, "indigo", "spreadsheetform_guides", "fund_v003.xlsx",
        ),
        "spreadsheet_form_guide_spec": load_guide_form_spec("fund_v003.xlsx"),
        "spreadsheet_form_guide_spec_versions": {
            1: load_guide_form_spec("fund_v001.xlsx"),
            2: load_guide_form_spec("fund_v002.xlsx"),
            3: load_guide_form_spec("fund_v003.xlsx"),
        },
        "fields": load_json_schema_fields("fund.json"),
    },
    "assessment_resource": {
        "json_schema": load_json_schema("assessment_resource.json"),
        "spreadsheet_form_guide": os.path.join(
            BASE_DIR,
            "indigo",
            "spreadsheetform_guides",
            "assessment_resource_v001.xlsx",
        ),
        "spreadsheet_form_guide_spec": load_guide_form_spec(
            "assessment_resource_v001.xlsx"
        ),
        "fields": load_json_schema_fields("assessment_resource.json"),
    },
}

CELERY_BROKER_URL = os.getenv("CLOUDAMQP_URL", "localhost")

APP_TITLE = os.getenv("APP_TITLE", "INDIGO")

API_SANDBOX_DATA_PASSWORD = os.getenv("API_SANDBOX_DATA_PASSWORD", "")

SENTRY_DSN = os.getenv("SENTRY_DSN")
if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN, integrations=[DjangoIntegration()],
    )

if "ON_HEROKU" in os.environ:
    import django_heroku

    django_heroku.settings(locals())
    DEBUG = False


else:

    import environ

    env = environ.Env(  # set default values and casting
        # SECURITY WARNING: keep the secret key used in production secret!
        JSONDATAFERRET_SECRET_KEY=(
            str,
            "lz@kp-&z6grz#fp#*!mi6c4-mozm)1u6m$57j%v21#u9l#lnog",
        ),
        JSONDATAFERRET_DEBUG=(bool, True),
        JSONDATAFERRET_ALLOWED_HOSTS=(list, []),
        JSONDATAFERRET_DATABASE_NAME=(str, "app"),
        JSONDATAFERRET_DATABASE_USER=(str, "app"),
        JSONDATAFERRET_DATABASE_PASSWORD=(str, "password"),
        JSONDATAFERRET_DATABASE_HOST=(str, "localhost"),
    )

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = env("JSONDATAFERRET_SECRET_KEY")

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = env("JSONDATAFERRET_DEBUG")

    ALLOWED_HOSTS = env("JSONDATAFERRET_ALLOWED_HOSTS")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("JSONDATAFERRET_DATABASE_NAME"),
            "USER": env("JSONDATAFERRET_DATABASE_USER"),
            "PASSWORD": env("JSONDATAFERRET_DATABASE_PASSWORD"),
            "HOST": env("JSONDATAFERRET_DATABASE_HOST"),
        }
    }

# This sets up S3 for file storage.
# If you are running locally don't set this and files will just appear on your local disk instead.
if os.getenv("AWS_ACCESS_KEY_ID", ""):
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME", "")
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "")
    AWS_S3_USE_SSL = True

from .base import *

DEBUG = True  # 暫時改為 True 來查看詳細錯誤信息

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '*']  # 開發環境可以用 '*'


# 添加日誌配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
    }
}
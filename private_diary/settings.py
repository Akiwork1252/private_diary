from .settings_common import *

# セキュリティーキーを生成して環境変数から読み込む
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# デバッグモードを無効
DEBUG = False

# 許可するホスト名リスト
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# 静的ファイルの設置場所
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

# Amazon SES関連設定
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'
# リージョン情報の指定
AWS_SES_REGION_NAME = 'us-west-2'
AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'

# ロギング
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガー設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        # Diaryアプリが使用するロガー
        'diary': {
            'handlers': ['file'],
            'level': 'INFO', 
        },
    },

    # ハンドラの設定
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',  # ログテーション感覚の単位(D=日)
            'interval': 1,  # ログテーション感覚(1日)
            'backupCount': 7,  # 保存しておくログファイル
        },
    },

    #  フォーマッタの設定
    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levalname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}


print("Environment ALLOWED_HOSTS:", os.environ.get('ALLOWED_HOSTS'))
print("Processed ALLOWED_HOSTS:", os.environ.get('ALLOWED_HOSTS', '').split(','))

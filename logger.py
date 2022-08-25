
# итоговое задание 13.4

LOGGING = {
    'version': 1,

    # контроль стандартной системы логирования
    'disable_existing_loggers': False,

    'style': '{',

    # фильтры
    'filters': {

        # для случая DEBUG = True
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },

        # для случаев DEBUG = False
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    # форматы сообщений
    'formatters': {
        'format_debug': {
            'format': '[%(asctime)s], %(levelname)s: %(message)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'format_warning': {
            'format': '[%(asctime)s], %(levelname)s: %(message)s, %(pathname)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'format_error': {
            'format': '[%(asctime)s], %(levelname)s: %(message)s, %(exc_info)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'format_critical': {
            'format': '[%(asctime)s], %(levelname)s: %(message)s, %(exc_info)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'format_general_log': {
            'format': '[%(asctime)s], %(levelname)s: %(message)s, %(module)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'format_errors_log': {
            'format': '[%(asctime)s], %(levelname)s: %(message)s, %(pathname)s, %(exc_info)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'format_security_log': {
            'format': '[%(asctime)s], %(levelname)s: %(message)s, %(module)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'format_email': {
            'format': '[%(asctime)s], %(levelname)s: %(message)s, %(pathname)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
    },

    # обработчики
    'handlers': {

        # отправляет в консоль уровень DEBUG
        'handler_console_debug': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'format_debug',
            'filters': ['require_debug_true'],
        },

        # отправляет в консоль уровень WARNING
        'handler_console_warning': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'format_warning',
            'filters': ['require_debug_true'],
        },

        # отправляет в консоль уровень ERROR
        'handler_console_error': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
            'formatter': 'format_error',
            'filters': ['require_debug_true'],
        },

        # отправляет в консоль уровень CRITICAL
        'handler_console_critical': {
            'class': 'logging.StreamHandler',
            'level': 'CRITICAL',
            'formatter': 'format_critical',
            'filters': ['require_debug_true'],
        },

        # отправляет в файл general.log
        'handler_file_general': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'filename': 'd:/logs/general.log',
            'formatter': 'format_general_log',
            'filters': ['require_debug_false'],
        },

        # отправляет в файл errors.log
        'handler_file_errors': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'filename': 'd:/logs/errors.log',
            'formatter': 'format_errors_log',
            'filters': ['require_debug_true'],
        },

        # отправляет в файл errors.log
        'handler_file_critical': {
            'class': 'logging.FileHandler',
            'level': 'CRITICAL',
            'filename': 'd:/logs/errors.log',
            'formatter': 'format_errors_log',
            'filters': ['require_debug_true'],
        },

        # отправляет в файл security.log
        'handler_file_security': {
            'class': 'logging.FileHandler',
            'filename': 'd:/logs/security.log',
            'formatter': 'format_security_log',
            'filters': ['require_debug_true'],
        },

        # отправляет по почте
        'handler_mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'formatter': 'format_email',
            'filters': ['require_debug_true'],
        },
    },

    # регистраторы
    'loggers': {

        'django': {
            'handlers': ['handler_console_debug',
                         'handler_console_warning',
                         'handler_console_error',
                         'handler_console_critical',
                         'handler_file_general',
                         ],
            'propagate': True,
        },

        'django.request': {
            'handlers': ['handler_file_error',
                         'handler_file_critical',
                         'handler_mail_admins',
                         ],
            'propagate': False,
        },

        'django.server': {
            'handlers': ['handler_file_error',
                         'handler_file_critical',
                         'handler_mail_admins',
                         ],
            'propagate': False,
        },

        'django.template': {
            'handlers': ['handler_file_error',
                         'handler_file_critical',
                         ],
            'propagate': False,
        },

        'django.db_backends': {
            'handlers': ['handler_file_error',
                         'handler_file_critical',
                         ],
            'propagate': False,
        },

        'django.security': {
            'handlers': ['handler_file_security',
                         ],
            'propagate': False,
        },
    }
}
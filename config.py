DEBUG = True  # For development purposes only

# Flask Redis
REDIS_URL = "redis://localhost:6379/0"

# Flask Mail Configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'test@example'
MAIL_PASSWORD = 'password'
MAIL_USE_TLS = False
MAIL_USE_SSL = True

# Database
POSTGRES = {
    'user': 'user',
    'password': 'password',
    'db': 'db',
    'host': 'localhost',
    'port': '5432',
}

POSTGRES_URL = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s'

#For development only
CRON='* 9-16 * * 0-6'

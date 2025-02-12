import os

db_config = {
    'mysql': {
        'driver': 'mysql',
        'host': os.getenv('DB_HOST', 'localhost'),
        'database': os.getenv('DB_NAME', 'your_database'),
        'port': int(os.getenv('DB_PORT', 3307)),
        'user': os.getenv('DB_USER', 'your_user'),
        'password': os.getenv('DB_PASSWORD', 'your_password'),
        'prefix': '',
    }
}

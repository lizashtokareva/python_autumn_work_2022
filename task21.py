
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

with open('config_default.txt', 'r') as f:
    lines = f.readlines()


with open('config_default.txt', 'w') as f:
    for line in lines:
        if '= ?' in line:
            parameter_name = line.split('=')[0].strip()
            if parameter_name in config_values:
                value = config_values[parameter_name]
                f.write(f'{parameter_name} = {value}\n')
            else:
                f.write(line)
        else:
            f.write(line)


f.close()
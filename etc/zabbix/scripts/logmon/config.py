log_file = '/var/log/zabbix/zabbix_agentd.log'
report = {
    'email': {
        'from': 'report@domain..com',
        'to': ['monitor@domain.com'],
        'smtp_server': 'smtp.gmail.com:587',
        'username': 'USERNAME@gmail.com',
        'password': 'YOUR_GMAIL_PASSWORD',
    }
}

rabbitmq = {
    'host': 'localhost'
}

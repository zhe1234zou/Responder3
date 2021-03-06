startup = {
	'mode'    : 'STANDARD',  # STANDARD or DEV or SERVICE
}

logsettings = {
	'log': {
		'version'   : 1,
		'formatters': {
			'detailed': {
				'class' : 'logging.Formatter',
				'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
			}
		},
		'handlers'  : {
			'console': {
				'class': 'logging.StreamHandler',
				'level': 'INFO',
			}
		},
		'root'      : {
			'level'   : 'INFO',
			'handlers': ['console']
		}
	}
}

servers = [
	{
		'handler'    : 'FTP',
	},
	{
		'handler'    : 'HTTP',
	},
	{
		'handler'    : 'SMTP',
	},
	{
		'handler'    : 'POP3',
	},
	{
		'handler'    : 'IMAP',
	},
	{
		'handler'    : 'KERBEROS',
	},
	{
		'handler'    : 'LDAP',
	},
	{
		'handler'    : 'VNC',
	},
	{
		'handler'    : 'SOCKS5',
	},
	{
		'handler'    : 'TELNET',
		'settings'   : {
			'banner' : '=========\r\nYou are being PWNd!\r\n=========',
		},
	},
	{
		'handler'  : 'SSH',
		'settings' : {
			'privkey_file' : '/home/responder/Desktop/Responder3/responder3/tools/ssh_server_test_cert.priv'
		},
	},

]
remote_manager = {
	'mode' : 'CLIENT',
	'config' : {},
	'server_url' : 'ws://127.0.0.1:9191',	
}

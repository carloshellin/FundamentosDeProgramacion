import smtplib

desde = 'chellincursopython@gmail.com'
hacia = 'correoPythonCurso@gmail.com'
titulo = 'GII_Tarde_Hellin_Carlos_email desde Python'

cabecera = 'From: %s\n' % desde
cabecera += 'To: %s\n' % hacia
cabecera += 'Subject: %s\n\n' % titulo
msg = "import smtplib\n\n\
desde = 'chellincursopython@gmail.com'\n\
hasta = 'correoPythonCurso@gmail.com'\n\
titulo = 'GII_Tarde_Hellin_Carlos_email desde Python'\n\n\
cabecera = 'From: %s\\n' % desde\n\
cabecera += 'To: %s\\n' % hasta\n\
cabecera += 'Subject: %s\\n\\n' % titulo\n\
msg = (el contenido de esta variable es este mensaje)\n\n\
# Datos\n\
username = 'chellincursopython@gmail.com'\n\
password = 'contraseña'\n\n\
# Enviando el correo\n\
servidor = smtplib.SMTP('smtp.gmail.com:587')\n\
servidor.starttls()\n\
servidor.login(username, password)\n\
servidor.sendmail(desde, hacia, cabecera + msg)\n\
servidor.quit()"

# Datos
username = 'chellincursopython@gmail.com'
password = 'contraseña'

# Enviando el correo
servidor = smtplib.SMTP('smtp.gmail.com:587')
servidor.starttls()
servidor.login(username, password)
servidor.sendmail(desde, hacia, cabecera + msg)
servidor.quit()

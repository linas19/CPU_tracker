# CPU_tracker
This tool allows the tracking of CPU usage and if CPU % usage value falls bellow a designated value an e-mail is sent to given e-mail. 

Prior to using the code update the following lines with your SMTP e-mail:

  mail.login('', '')
  mail.sendmail('', target_mail, content)

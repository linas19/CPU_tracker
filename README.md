# CPU_tracker
This tool allows the tracking of CPU usage and if CPU % usage value falls bellow a designated value an e-mail is sent to given e-mail. 
This is useful when information about a finished computer simulation is needed.  

Prior to using the code update lines 22 and 23 with your SMTP e-mail:

  mail.login('example@example.com', 'examplepassword')
  mail.sendmail('example@example.com', target_mail, content)

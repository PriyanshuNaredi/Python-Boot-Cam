import smtplib

my_email = "linuxrdb007@gmail.com"
password = "cuzm rset fwpn ytxe"


connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="linuxrdp007@gmail.com",msg="Subject:Hello\n\n This is")

connection.close()

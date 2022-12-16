import requests
import smtplib


email_add = "anuj.pundir@copperchipsinc.com"
password  = ""
email_a = "pundir.anuj@gmail.com"

def send_email1():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_add, password)
    subject = "!!!!!! Direct Pulse Transaction is down"
    body = "Please check Pulse Direct Transaction" , word1
    message = f'Subject: {subject}\n\n {body}'
    s.sendmail(email_a, email_a, message)
    s.quit()

def send_email2():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_add, password)
    subject = "!!!!!! Shopify Pulse Transaction is down"
    body = "Please check Shopify Pulse Transaction" ,word2
    message = f'Subject: {subject}\n\n {body}'
    s.sendmail(email_a, email_a, message)
    s.quit()    

producturl1="http://10.47.65.72:5001/api/pulse/direct"
producturl2="http://10.47.65.72:5001/api/pulse/shopify"

res1 = requests.get(producturl1, timeout=20)
res2 = requests.get(producturl2, timeout=20)

print("The Status Code is :" , res1.status_code)
if res1.status_code != 200:
    send_email()

word1 =res1.text
word2 =res2.text

if word1.find('Declined') != -1:
    print("Direct Transaction is OK ")
elif word1.find('Guaranteed') != -1: 
    print("Direct Transaction is OK")    
elif word1.find('Approved') != -1: 
    print("Direct Transaction is OK")
else:
    print("Direct Transaction is failed")
    send_email1()


if word2.find('Declined') != -1:
    print("Shopify Transaction Status is OK")
elif word2.find('Guaranteed') != -1: 
    print("Shopify Transaction Status is OK")    
elif word2.find('Approved') != -1:
    print("Shopify Transaction Status is OK")
else:
    print("Shopify Transaction Status is failed")
    send_email2()



#data_dict1 = json.loads(res1.text)
#data_dict2 = json.loads(res2.text)

#for element in res1.text:
     
 #   if element=="Guaranteed" or element=="Declined": 
       # print("Pulse Direct Transaction is OK")
        #break
#else:
  #send_email()


  

#score1 = data_dict1['Complete']['res_body']['data']['evaluationDecision']
#score2 = data_dict2['Complete']['res_body']['data']['score']

#if score1=="Guaranteed" or score1=="Declined":
    # print("Pulse Direct Transaction is :" , score1)      
#else:
   #send_email()   

#if score2==0:
 #  send_email()
  # print("please check Pulse Shopify Trans")
#else:
 # print("The Shopify Transaction score is :" , score2)    

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Canon-Mirrorless-Digital-RF-S18-150mm-Stabilisation/dp/B0B2KV6D97/ref=sr_1_3?dib=eyJ2IjoiMSJ9.xy7ERz0rD65MMD8FBWsssg9yJgZmA7xPpTJaJDQjcXorNVQ4oIkqsFUZi-k7xpPbgHz5eTnNBbzW2T9ygAN98bNmfz23GlpMJt8SF_HnNjm4Ae6qnT7zbS_tS2WeKngrIaMJcHMtsI9Kk5oC8V2b_da_XMBffH2RIGwwp6XL7Sd7xAKD-aFtbddlVdKXZk1O1VIaKQoAT1j-ecDecOR-_R8NfnRwsoSf4ERAI_EF9CJBLFdmdPT9WyzWfs_nRDlv.ioxURf2LWvTIx2YGQfy4J_lfVmjoUfYG4BBRoSQcdXs&dib_tag=se&pf_rd_i=1388977031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=aec9df84-1cda-4606-b9b6-27ae4c84c098&pf_rd_r=ERSYP1VGFVW964EKE9CA&pf_rd_s=merchandised-search-6&qid=1724922407&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0'}

def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_outprice").get_text()
    converted_price = price[0:6]

if(converted_price < 50000):
    send_mail()

print(converted_price)
print(title.strip())

if(converted_price < 50000):
    send_mail()


def send_mail():
    server = stmplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.echlo()
     
    server.login('')
    subject = 'Notify price down'
    body = 'Check the amazon link https://www.amazon.in/Canon-Mirrorless-Digital-RF-S18-150mm-Stabilisation/dp/B0B2KV6D97/ref=sr_1_3?dib=eyJ2IjoiMSJ9.xy7ERz0rD65MMD8FBWsssg9yJgZmA7xPpTJaJDQjcXorNVQ4oIkqsFUZi-k7xpPbgHz5eTnNBbzW2T9ygAN98bNmfz23GlpMJt8SF_HnNjm4Ae6qnT7zbS_tS2WeKngrIaMJcHMtsI9Kk5oC8V2b_da_XMBffH2RIGwwp6XL7Sd7xAKD-aFtbddlVdKXZk1O1VIaKQoAT1j-ecDecOR-_R8NfnRwsoSf4ERAI_EF9CJBLFdmdPT9WyzWfs_nRDlv.ioxURf2LWvTIx2YGQfy4J_lfVmjoUfYG4BBRoSQcdXs&dib_tag=se&pf_rd_i=1388977031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=aec9df84-1cda-4606-b9b6-27ae4c84c098&pf_rd_r=ERSYP1VGFVW964EKE9CA&pf_rd_s=merchandised-search-6&qid=1724922407&sr=8-3' 

    msg = f"subject: {subject}\n\n{body}"
        
    server.sendmail(
        'krishnasai234.ksr@gmail.com',

        msg 
    )
    print ('EMAIL SENT!')
    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)

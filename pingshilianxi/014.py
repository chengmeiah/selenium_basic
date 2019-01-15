from selenium import webdriver
import requests,base64
import time
 
driver = webdriver.Chrome()
driver.get('https://persons.shgjj.com/')
time.sleep(2)
image_ele = driver.find_element_by_css_selector('#img1')
image_ele.screenshot('image.png')

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=s45AcfuqnLNfNBIy2XDza78w&client_secret=5hzBM6tqxnFUcQEHCLSVClpi1QoaHZUV'
res = requests.get(host)
r = res.json()

access_token = r['access_token']
print(access_token)

 
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/idcard?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'image.png', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
imageres = requests.post(url,data=params)
image_json = imageres.json()
print(image_json)
print(imageres.json())

image_num = image_json['words_result'][0]['words']
driver.find_element_by_id('imagecodel').send_keys(image_num)
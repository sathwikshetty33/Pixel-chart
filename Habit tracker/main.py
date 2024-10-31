import requests
import datetime
username='sathwikshetty'
Token = ''
pixeluser={
    'token' : Token,
    'username': username,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',
}
# res = requests.post(url='https://pixe.la/v1/users',json=pixeluser)
# print(res.text)
postparams={
    'id' : 'wertyuiolkj',
    'name' : 'shettygraph',
    'unit' : 'hour',
    'color' : 'sora',
    'type' : 'float',
}
headers={
'X-USER-TOKEN' : Token,
}
today = datetime.datetime.now()

progress={
    'date': today.strftime("%Y%m%d"),
    'quantity': '5',
}
update={
'quantity': '6'
}
# res1= requests.post(url=f'https://pixe.la/v1/users/{username}/graphs',json=postparams,headers=headers)
# print(res1.text)
res2=requests.post(url=f"https://pixe.la/v1/users/{username}/graphs/{postparams['id']}",headers=headers,json=progress)
print(res2.text)
# res2=requests.put(url=f"https://pixe.la/v1/users/{username}/graphs/{postparams['id']}/{today.strftime('%Y%m%d')}",headers=headers,json=update)
# print(res2.text)
# res2=requests.delete(url=f"https://pixe.la/v1/users/{username}/graphs/{postparams['id']}/{today.strftime('%Y%m%d')}",headers=headers)
# print(res2.text)
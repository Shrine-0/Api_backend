import os
import pprint
from veryfi import Client
import json 



# pip install veryfi

# client_id = 'vrfkdoOfZ8htFzfIoPhOyRslrSvSUGiYuAdIeX2'
# client_secret = 'HmcBW0s6DzFMeeB6woHgg0iMLm5KFRXt50vIOUl0sZ2jtmycpDHcyx7uwBk4VGY76aj82Dpu3aa5Mt50HIHS4TjJCoXgDTnFjsw1sJWEc8HS0zAAmAteyTBPMPhs3ZdA'
# username = 'nischalthapa10'
# api_key = 'c5a359032820c1336ad35923e60a6185'
__path  = './Media_files'
with open ('./Api_keys.json') as f :
    data = json.load(f)
    
client_id = data['client_id']
client_secret =data['client_secret']
username = data['username']
api_key = data['api_key']
#client = veryfi.Client(client_id, client_secret, username, api_key)

veryfi_client = Client(client_id, client_secret, username, api_key)
#process_document() for all the files in media_files folder using a loop  
file_list = []
for filename in os.listdir(__path):
    if filename.endswith(('.png','.jpg','.jpeg')):
        file_list.append(filename)
# print(file_list[1])


json_result = veryfi_client.process_document(os.path.join(__path,file_list[1]),
                                      categories=['travel', 'airfare', 'hotel', 'meals', 'job supplies and materials',
                                                  'grocery'])
                                      
# latest_file = max(os.listdir(__path), key=os.path.getctime)#getctime returns the time of last modification of path
# if latest_file.endswith(('.png','.jpg','.jpeg')):
#     json_result = veryfi_client.process_document(os.path.join(__path,latest_file),
#                                     categories=['travel', 'airfare', 'hotel', 'meals', 'job supplies and materials',
#                                                 'grocery'])
pprint.pprint(json_result)


#adding the result to json file format 

file_path = 'Result.json'  

with open(file_path,'w') as json_file: #The with statement ensures that the file is automatically closed when the block of code inside it is exited.
    json.dump(json_result,json_file)
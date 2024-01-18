#headers keyword is X-USER-TOKEN or X_AUTH_TOKEN or some of the sort where needed
import requests
import datetime

########### Create Acc #############
USERNAME = "vaporbirdo"
TOKEN = "ojghiyt2fghwqeih4u785F45ouhfbid"
GRAPH_ID = "graph1"
pixela_url = "https://pixe.la/v1/users"

parameters = {
    "username" : USERNAME,
    "token" : TOKEN,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
 }

#sign_up = requests.post(url = pixela_url, json = parameters)
#print(sign_up.text)

########### Create Graph ############
graph_url = f"https://pixe.la//v1/users/{USERNAME}/graphs"
graph_params = {
    "id" : GRAPH_ID,
    "name" : "calories daily",
    "unit" : "kcal",
    "type" : "int",
    "color" : "ichou",
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}   

#create_graph = requests.post(url = graph_url, json = graph_params, headers = headers)
#print(create_graph.text)

############# Add Data ############
add_url = f"https://pixe.la//v1/users/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.datetime.now()
#today_str = str(today.year) + str("{:02d}".format(today.month)) + str("{:02d}".format(today.day))
today_str = today.strftime("%Y%m%d")
add_params = {
    "date" : today_str,
    "quantity" : "1000",
#    "OptionalData" : '{"I don\'t know" : "what this is"}',
}
#Pixela think they are cool blocking 25% of the requests
while True:
    try:
       # add_pixel = requests.post(url = add_url, json = add_params, headers = headers)
       # add_pixel.raise_for_status()
        break
    except requests.exceptions.HTTPError:
        continue
    finally:    
        pass
        #print(add_pixel.text)

############### Update Pixel ##############
update_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today_str}" 
update_params = {"quantity" : "3000"}

#update_pixel = requests.put(url = update_url, json = update_params, headers = headers)
#print(update_pixel.text)

################ Delete Pixel ##############
delete_url = update_url
delete_pixel = requests.delete(url = update_url, headers = headers)
print(delete_pixel.text)

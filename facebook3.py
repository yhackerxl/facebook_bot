import facebook 

image = "https://yhackerxl.bio/logo.svg"

message ="yhackerxl image"
id = 104713542060157
token = 
graph=facebook.GraphAPI(access_token=token)
x=graph.put_object(id, "photo",message,url=image)
print(x)
print("photo sent")
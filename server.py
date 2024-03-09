from flask import Flask, request
import json

app = Flask (__name__)#__name__ this is using the name of the folder

@app.get("/")
def home():
    return "Hello from Flask"
# hello

@app.get("/testing")
def test():
    return "hello from another page"

# create 2 more API (about and blog)
@app.get("/about")
def about():
    me = {"name": "Ricardo Hurtado"}
    return json.dumps(me)

@app.get("/blog")
def blog():
    return "Dont read me"

@app.get("/version")
def version():
    version = {"name": "mouse", "version": "2","build":123456}
    return json.dumps(version)

# this time we need to read and write in to the server
products = []
@app.get("/api/products")
def get_products():

    return json.dumps(products)

#post writes 
@app.post("/api/products")
def save_products():
    #this should save an new product
    product = request.get_json()
    print (product)
    #mock the save
    products.append(product)
    return json.dumps(product)


app.run(debug=True)#This apply changes on the code , live



# API / Endpoints 
#transforn JSON / convent JSON in an object again

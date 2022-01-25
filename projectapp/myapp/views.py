from django.shortcuts import render,redirect
from pymongo import MongoClient
connection_string='mongodb://127.0.0.1:27017/'
client=MongoClient(connection_string)


# Create your views here.
def login(request):

    if request.method=='POST':
       
        print(client.list_database_names())
        mydb = client["users"]
        mycol = mydb["userdetails"]
        print(mycol)


        username=request.POST.get('username')
        password=request.POST.get('password')
        myquery={'username': username,'password':password }
        if (mycol.find(myquery)):
            f=0
            for x in mycol.find(myquery):
               f+=1
            if f>0:    
               return redirect('dashboard')
        print("Login")
        return render(request,'login.html',{'msg':["please login again"]})

    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       email=request.POST.get('email')
       myquery={'username': username}

       mydb = client["users"]
       mycol = mydb["userdetails"]

       if (mycol.find(myquery)):
           f=0
           for x in mycol.find(myquery):
               f+=1
           if f>0:    
               return render(request,'register.html',{"msg":"Username already exist"})
       
       mydict = { "username": username, "password": password ,"email" :email}
       mycol.insert_one(mydict)
       return render(request,'login.html')
    return render(request,'register.html')

def dashboard(request):
    if request.method=='POST':
        print("loggedout")
        return redirect('/')   

    return render(request,'dashboard.html')        

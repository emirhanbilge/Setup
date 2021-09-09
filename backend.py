from flask import Flask
from flask import render_template , redirect
from flask import request
from flask import redirect 
import sys  

sys.path.append('../')
sys.path.append('./')
from flask import Flask, redirect, url_for, request
from networkRunner import sendNetwork , writedhcp

app = Flask(__name__ ,static_url_path='/static')




@app.route('/')
def index():
    return render_template("index.html")



@app.route('/saveSettings' ,methods = ['POST', 'GET'])
def saveSettings():


    if request.method == 'POST':
      
        if  request.form["gateway"] != "a":
            arr = request.form["ip"].split(".")[0:3]
            arr.append(1) 
            gateway = ""
            for i in range(len(arr)-1):
                gateway += str(i)+"."
            gateway += str(arr[len(arr)-1] )
            sendNetwork(request.form["ip"] ,request.form["subnetMask"],request.form["gateway"] )
        else:
            sendNetwork(request.form["ip"] ,request.form["subnetMask"] , request.form["gateway"]  )

    return render_template("index.html")

@app.route('/dhcp')
def dhcp():
    writedhcp()
    return render_template("finish.html")



if __name__ == "__main__":
    app.run(debug=True)
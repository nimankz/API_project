from flask import Flask
import mainProject
import requests
my_dict={}
my_currency=mainProject.crypto()
app=Flask(__name__)
@app.route("/")
def initialize():
    try:
        m=my_currency.fristOpen()
        # pp(m
        global my_dict 
        my_dict=m
        print(m)
        return m
        
    except:
        return "We have a little problem,please wait before you try again."
@app.route("/<name>",methods=["GET"])
def crypto(name):
    if requests.method=="GET":
        try:
            url=my_currency.goToPage(name)
            return [my_dict[name],f"at this moment:{my_dict['time']}",f"for seeing more information go to this page:{url}"]
        except:
            return "We have a little problem,please wait before you try again."

if __name__=="__main__":
    app.run()



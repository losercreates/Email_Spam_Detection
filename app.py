from flask import Flask, render_template, request
import spamemail as sm

app=Flask(__name__)

@app.route("/")
def submit():
    return render_template("index.html")

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        input_mail=request.form['input_mail']
        input_mail=[input_mail]
        email=sm.spam_email_prediction(input_mail)
        etype=email
        
    return render_template("index.html",email_type=etype)




if __name__=="__main__":
    app.run(debug=True)
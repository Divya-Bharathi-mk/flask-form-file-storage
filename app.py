from flask import Flask,render_template,request
app=Flask(__name__)

data ={
    "company":"Velon Interiors",
    "name"   :"Divya"
}

@app.route('/')
def home():
    return render_template("home.html",**data)

@app.route('/home')
def home_page():
    return render_template("home.html",**data)

@app.route('/about')
def about():
    return render_template("about.html",**data) 

@app.route('/contact',methods=['GET','POST'])
def contact():
    message=None
    if request.method=='POST':
        user_name=request.form.get('name')
        mail=request.form.get('email')
        text=request.form.get('message')
        print(user_name)
        print(mail)
        print(text)
        with open("data.txt", "a") as file:
            file.write(f"name:{user_name} | email:{mail} | text:{text}\n")
        message="Form Submit Successfully"
    return render_template("contact.html",**data,message=message)

    

if __name__ == "__main__":
    app.run(debug=True)
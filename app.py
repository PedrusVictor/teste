from flask import Flask,redirect, render_template

app=Flask(__name__)
name="teste"
@app.route("/")
def main():
    return render_template('index.html',name=name)

if  __name__=="__main__":
    app.run()
    

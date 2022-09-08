from flask import *
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/sign_up')
def test():
  return render_template('signup.html') 


@app.route('/setcookie',methods = ['POST'])  
def setcookie():
  if request.method == 'POST':
    username = request.form['username']  
    password = bcrypt.generate_password_hash(request.form['password']) 

    resp = make_response(render_template('login.html'))  
    resp.set_cookie('email',username) 
    resp.set_cookie('password',password)

    return resp 
         

@app.route('/getcookie',methods = ['POST'])  
def getcookie():  
    if request.method == "POST":  
        fusername = request.form['username']  
        fpassword = request.form['password']  

    if fusername in request.cookies.get('email') and bcrypt.check_password_hash(request.cookies.get('password'), fpassword):    
      return  render_template('home.html',message=fusername)
    else:  
      error="wrong Credential :("
      return render_template('login.html', error=error)       

if __name__ == '__main__':
  app.run(debug=True)
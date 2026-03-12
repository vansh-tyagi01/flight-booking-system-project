from flask import Flask,request,redirect,url_for,session,Response
loginPage=Flask(__name__)
loginPage.secret_key ="supersecret"

@loginPage.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "kanhaiya" and password == "812623":
            session["user"] =username # store in session.
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid details! Please try again",mimetype="text/plain") #By default return text/html when we are not write mimetype.
        
    return '''
            <h2>Login Page</h2>
            <form method="POST">
            Username : <input type="text" name="username"><br>
            password : <input type="password" name="password"><br>
            <input type="submit" value="Login">
            </form>
'''

@loginPage.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome, {session["user"]}</h2>
            <a href="{url_for('logout')}">Logout</a>
    '''
    return redirect(url_for("login"))

# logout

@loginPage.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))


loginPage.run(debug=True)

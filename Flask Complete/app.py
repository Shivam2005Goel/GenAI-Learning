from flask import Flask,redirect,url_for,render_template,request


#WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello Welcome to Shivam Goel's SIH Flask App"

@app.route('/members')
def function():
    return "Hello you are a member of this site"

@app.route('/dashboard')
def dashboard():
    return 

@app.route('/success/<int:score>')
def find_score1(score):
    return "The persona has passed the exam and the score is" + str(score)

@app.route('/fail/<int:score>')
def find_score2(score):
    return "Person has failed with the score of" + str(score)

@app.route('/results/<float:marks>')
def check(marks):
    if(marks > 50):
        return render_template("result.html",res = "PASS",marks = marks)
    elif(marks < 50):
        return render_template("result.html", res = "FAIL",marks = marks)

@app.route('/learnhtml')
def learninghtml():
    return render_template("index.html")

@app.route('/submit',methods = ['GET','POST'])
def submitcheck():
    total_score = 0
    if(request.method == 'POST'):
        maths = int(request.form['maths'])
        science = int(request.form['science'])
        english= int(request.form['english'])
        hindi = int(request.form['hindi'])    
        total_avg = float(maths + science + english + hindi) / 4
        # if(total_avg > 50):
        return redirect(url_for('check',marks = total_avg))
        # elif(total_avg < 50):
            # return redirect(url_for('check',marks = total_avg))
            # return redirect(url_for('check',marks = total_avg))
    else:
        return render_template("index.html")

        

if __name__ == '__main__':
    app.run(debug = True)


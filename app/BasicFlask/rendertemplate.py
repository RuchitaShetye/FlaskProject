from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def index():
    name="Hello,Welcome"
    ls=[21,11,23,31,134]
    tup=(21,13,22,44)
    dic={'a':21,'b':33}
    result={'eng':50,'math':59}
    return render_template('tmp1.html',name=name,list1=ls,tups=tup,dic=dic,result=result)

if __name__=='__main__':
    app.run(debug=True)

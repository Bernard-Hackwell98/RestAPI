from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to my world"

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n =n
    while(n>0):
        digit = n%10
        sum += digit**order
        n = n//10
    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result={
            "Number": n,
            "Armstrong":True
        }
    else:
        print(f"{copy_n} is an not armstrong number")
        result={
            "Number": n,
            "Armstrong":False
        }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True)
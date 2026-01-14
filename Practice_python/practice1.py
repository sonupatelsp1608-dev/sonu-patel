from flask import Flask, jsonify

app=Flask(__name__)

data={
    "name":"sonu",
    "age":20,
    "location":"parel",
    "address":"Mumbai"
}

@app.route("/home")
def show():
    return jsonify(data)
    
if __name__=='__main__':
    app.run(debug=True)
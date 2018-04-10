from flask import jsonify,request
from flask import Flask
import deepcut

#License 

app = Flask(__name__)

#UTF-8
app.config['JSON_AS_ASCII'] = False



@app.route("/hello")
def hello():
	data = request.args.get("source")
	token = deepcut.tokenize(data)

	return jsonify(
		source=data,
		tokenize=token
    )

	
@app.route('/json')
def json():
    return jsonify(
        username='Tan',
        email='tanyas@tot.co.th',
        id=11
    )
	
if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)
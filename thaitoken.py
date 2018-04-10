from flask import Flask,jsonify,request
import deepcut

#License 

app = Flask(__name__)

#UTF-8
app.config['JSON_AS_ASCII'] = False



@app.route("/tokenize", methods=["GET", "POST"])
def tokenize():
	if request.method == 'POST':
		data = request.form['source']
	elif request.method == 'GET':
		data = request.args.get('source')
	return thaitoken_deepcut(data);


def thaitoken_deepcut(data):
	token = deepcut.tokenize(data)
	return jsonify(
		source=data,
		tokenize=token
    )

@app.route('/about')
def about():
    return jsonify(
        WebServiceDeveloper='Tanya S.',
        email='tanyas@tot.co.th',
        github="",
		PullDeepcutFrom="https://github.com/rkcosmos/deepcut"
    )
	
if __name__ == "__main__":
    #app.debug = True
    app.run(host = '0.0.0.0',port=process.env.PORT )

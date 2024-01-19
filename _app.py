from flask import Flask, jsonify,request

app = Flask(__name__)


@app.route("/<string:name>")
def starter_api(name: str):
    #name=request.args.get("name")
    return jsonify(data=name),200


if __name__ == "__main__":
    app.run()

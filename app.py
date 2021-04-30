from flask import Flask, render_template,request,jsonify,redirect,url_for
import pyqrcode
import png
from pyqrcode import QRCode

app = Flask(__name__)
PORT= 4006

@app.route('/',methods=["POST","GET"])
def hello_world():
    return  render_template("index.html", title="URL TO QRCODE CONVERTER")

@app.route('/downloads',methods=["POST","GET"])
def downloads():
    url_link = request.values.get("url","")
    url = pyqrcode.create(url_link)
    url.png("static/image/qrcode.png",scale=6)
    #return ("downloaded successfully")
    return  render_template("show.html", title="Download QR code")

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port = PORT)

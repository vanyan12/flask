from pdf import generate_test

from flask import Flask, request

from flask import send_file

from fpdf import FPDF
import os

from zipfile import ZipFile, ZIP_DEFLATED

import Data

from feedback import send_feedback


app = Flask(__name__)


@app.route("/")
def welcome():
    return "Un bon coup!"

@app.route("/generate-<fac>")
def generate_tests_for_facs(fac):

    timestamp = generate_test(fac)

    # return {'test_url': f"/Users/van/Desktop/Server/Files/Math_test_{fac}_{timestamp}.pdf",

    #         "answer-url": f"/Users/van/Desktop/Server/Files/Answer_{fac}_{timestamp}.pdf"}

    zipf = ZipFile(f"./Files/Math-test-{fac}-{timestamp}.zip", 'w', compression=ZIP_DEFLATED)


    for file in (f"./Files/Math_test_{fac}_{timestamp}.pdf", f"./Files/Answers_{timestamp}.pdf"):

        zipf.write(file, os.path.relpath(file, "C://Users/van/Desktop/Server/Files"))
    

    zipf.close()

    return {"stamp": timestamp}



@app.route("/Users/van/Desktop/Server/Files/Math-test-<fac>-<timestamp>.zip")

def send_IMA_test(fac, timestamp):

    for file in os.listdir(os.path.join(os.getcwd(),"Files")):

        if file.endswith("pdf") and timestamp in file:

            os.remove(os.path.join(os.getcwd(), f"Files/{file}"))

    return send_file(f"C://Users/van/Desktop/Server/Files/Math-test-{fac}-{timestamp}.zip", as_attachment=True, mimetype="application/zip")



@app.route("/manual", methods=['POST'])

def manual():

    sections = request.json["sections"]

    Data.Faculties["manual"] = sections

    timestamp = generate_test("manual")


    zipf = ZipFile(f"./Files/Math-test-{timestamp}.zip", 'w', compression=ZIP_DEFLATED)


    for file in (f"./Files/Math_test_{timestamp}.pdf", f"./Files/Answers_{timestamp}.pdf"):

        zipf.write(file, os.path.relpath(file, "C://Users/van/Desktop/Server/Files"))
    

    zipf.close()

    return {"stamp": timestamp}



@app.route("/Users/van/Desktop/Server/Files/Math-test-<timestamp>.zip")

def send_manual_test(timestamp):

    for file in os.listdir(os.path.join(os.getcwd(),"Files")):

        if file.endswith("pdf") and timestamp in file:

            os.remove(os.path.join(os.getcwd(), f"Files/{file}"))
    

    return send_file(f"C://Users/van/Desktop/Server/Files/Math-test-{timestamp}.zip", as_attachment=True, mimetype='application/zip')



@app.route("/clean/<stamp>")

def clean(stamp):

    for file in os.listdir(os.path.join(os.getcwd(),"Files")):

        if file.endswith("zip") and stamp in file:

            os.remove(os.path.join(os.getcwd(), f"Files/{file}"))


    return {"msg": "Files folder is cleaned"}


@app.route("/feedback", methods=['POST'])

def send():

    data = request.json

    send_feedback(data['email'], data['msg'])
    return " "



if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000, debug=True)
    
    


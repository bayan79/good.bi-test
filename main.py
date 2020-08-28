import os
import pandas as pd

from flask import Flask, request, render_template, jsonify


TEMPLATE_FILE = "data_json.html"


application = Flask(__name__)


@application.errorhandler(500)
def error_handler(error):
    print(error)
    return "Sorry! We are working on problem..."


@application.route("/", methods=['GET'])  
def root():
    data_file = os.getenv('MYAPP_DATAFILE', "titanic.csv")
    df = pd.read_csv(data_file)
    table = df.to_html(classes='mystyle', header=True, table_id="table")
    return render_template(TEMPLATE_FILE, table=table)


@application.route("/data.json" , methods=['GET'])  
def data_json():

    return {}

        

if __name__ == "__main__":

    port = int(os.getenv('MYAPP_PORT', 5000))
    application.run(debug=os.getenv('MYAPP_DEBUG', True), port=port, host='0.0.0.0')




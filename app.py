from flask import Flask, redirect, render_template
from pymongo import MongoClient

import pandas as pd
import numpy as np
from plots import *

app =  Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("website.html")

@app.route('/refresh_plots', methods=['GET'])



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os
print("Arquivo existe?", os.path.exists("SampleSuperstore.csv"))


app = Flask(__name__)
CORS(app)

@app.route('/api/vendas')
def get_vendas():
    try:
        df = pd.read_csv("SampleSuperstore.csv")
        df = df.fillna("")
        vendas = df.to_dict(orient="records")
        return jsonify(vendas)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)

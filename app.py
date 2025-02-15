from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend access

# Google Sheets API URL
GOOGLE_SHEET_API_URL = "https://script.google.com/macros/s/AKfycbxFDCl6aKPLLmLmupFVgswSpHCODth4_gVCi34RbrsqL_SdU_pGSG2ic2MBI4-B-mcF/exec"

@app.route("/get_prices", methods=["GET"])
def get_prices():
    try:
        response = requests.get(GOOGLE_SHEET_API_URL)
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)  # Return the fetched data to the frontend
        else:
            return jsonify({"error": "Failed to fetch data from Google Sheets"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

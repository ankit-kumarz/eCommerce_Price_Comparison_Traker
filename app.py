from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS to allow frontend access

# Google Sheets API URL
GOOGLE_SHEET_API_URL = "https://script.google.com/macros/s/AKfycbxFDCl6aKPLLmLmupFVgswSpHCODth4_gVCi34RbrsqL_SdU_pGSG2ic2MBI4-B-mcF/exec"

@app.route("/")
def index():
    """Serve the main index.html file"""
    return send_from_directory('.', 'index.html')

@app.route("/pages/<path:filename>")
def serve_pages(filename):
    """Serve pages from the pages folder"""
    return send_from_directory('pages', filename)

@app.route("/styles/<path:filename>")
def serve_styles(filename):
    """Serve CSS files from the styles folder"""
    return send_from_directory('styles', filename)

@app.route("/scripts/<path:filename>")
def serve_scripts(filename):
    """Serve JavaScript files from the scripts folder"""
    return send_from_directory('scripts', filename)

@app.route("/assets/<path:filename>")
def serve_assets(filename):
    """Serve assets from the assets folder"""
    return send_from_directory('assets', filename)

@app.route("/<path:filename>")
def serve_root_files(filename):
    """Serve files from the root directory (for images and other assets)"""
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    return "File not found", 404

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

from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)

# HTML form for manual CSV upload
UPLOAD_FORM = """
<!doctype html>
<html>
<head>
    <title>Upload CSV</title>
</head>
<body>
    <h2>Upload CSV File Manually</h2>
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file" accept=".csv"><br><br>
        <input type="submit" value="Upload CSV">
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    # Show upload form
    return render_template_string(UPLOAD_FORM)

@app.route("/upload", methods=["POST"])
def upload_csv():
    if "file" not in request.files:
        return "No file uploaded!", 400

    file = request.files["file"]

    if file.filename == "":
        return "No file selected!", 400

    try:
        # Read CSV into pandas DataFrame
        df = pd.read_csv(file)

        # Show first 5 rows and columns
        return f"""
        <h3>CSV Uploaded Successfully </h3>
        <p>Columns: {', '.join(df.columns)}</p>
        <p>First 5 rows:</p>
        {df.head().to_html()}
        """
    except Exception as e:
        return f"Error reading CSV: {e}", 400

if __name__ == "__main__":
    app.run(debug=True)

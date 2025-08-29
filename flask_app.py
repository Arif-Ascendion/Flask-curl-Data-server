from flask import Flask, request, redirect, url_for
import csv
import io

app = Flask(__name__)

uploaded_data = None
current_index = 0

@app.route('/')
def index():
    global uploaded_data, current_index

    if uploaded_data is None:
        return "<h2>Waiting for CSV upload... Use curl or BAT file to upload your file.</h2>"

    # Show rows up to current_index
    rows_to_display = uploaded_data[:current_index]

    table_html = "<h2>CSV Rows Displayed:</h2><table border='1'>"
    for row in rows_to_display:
        table_html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
    table_html += "</table>"

    html = f"{table_html}<br>"

    # Auto-refresh every 5 seconds to show next row
    if current_index < len(uploaded_data):
        html += """
        <script>
            setTimeout(function() {
                fetch('/next', {method: 'POST'})
                .then(() => window.location.reload());
            }, 5000);
        </script>
        """
    else:
        html += "<h3>All rows displayed!</h3>"

    return html

@app.route('/next', methods=['POST'])
def next_row():
    global current_index, uploaded_data
    if uploaded_data and current_index < len(uploaded_data):
        current_index += 1
    return '', 204  # Return empty response for fetch

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    global uploaded_data, current_index
    file = request.files.get('file')
    if not file:
        return "No file uploaded", 400

    # Read CSV
    stream = io.StringIO(file.stream.read().decode("utf-8"))
    reader = csv.reader(stream)
    uploaded_data = list(reader)
    current_index = 1  # Start showing from first row automatically

    return "CSV uploaded successfully! Open http://127.0.0.1:5000/ to view."

if __name__ == '__main__':
    app.run(debug=True)

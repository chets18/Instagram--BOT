from flask import Flask, render_template_string, request, jsonify, send_file
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from docx import Document
import json
import io

# A small screen
app = Flask(__name__)

@app.route("/")
def show_data():
    with open("data.json", "r") as f:
        data = json.load(f)
    html = html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> Instagram BOT</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f7fa;
        }

        .sidebar {
            height: 100vh;
            width: 220px;
            position: fixed;
            background-color: #1f2a40;
            color: white;
            padding-top: 20px;
        }

        .sidebar h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #ffcc00;
        }

        .sidebar a {
            padding: 12px 25px;
            display: block;
            color: white;
            text-decoration: none;
        }

        .sidebar a:hover {
            background-color: #30405f;
        }

        .topbar {
            margin-left: 220px;
            background-color: #fff;
            padding: 15px 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .topbar h1 {
            margin: 0;
            font-size: 24px;
            color: #333;
        }

        .main {
            margin-left: 220px;
            padding: 30px;
        }

        .cards {
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
        }

        .card {
            flex: 1;
            background-color: #fff;
            border-left: 6px solid #ffcc00;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .card h3 {
            margin: 0 0 10px;
            font-size: 18px;
            color: #333;
        }

        .card p {
            margin: 0;
            font-size: 22px;
            font-weight: bold;
            color: #1f2a40;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }

        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ccc;
        }

        th {
            background-color: #ffcc00;
            color: #1f2a40;
        }

        .button {
            background-color: #ff9900;
            color: white;
            border: none;
            padding: 8px 12px;
            cursor: pointer;
            border-radius: 4px;
        }

        .button:hover {
            background-color: #ffaa33;
        }

        .export-btn {
            background-color: #1f2a40;
            margin-top: 15px;
        }

        .export-btn:hover {
            background-color: #354a6e;
        }
    </style>
</head>
<body>
    <div class="sidebar">
        <h2>⚡ BOT</h2>
        <a href="/">Dashboard</a>
        <a href="#">Reports</a>
        <a href="#">Users</a>
        <a href="#">Settings</a>
    </div>
    <div class="topbar">
        <h1>Your Dashboard Overview</h1>
        <div>Welcome 👋</div>
    </div>
    <div class="main">
        <div class="cards">
            <div class="card"><h3>Online Users</h3><p>--</p></div>
            <div class="card"><h3>Total Users</h3><p>{{ data|length }}</p></div>
            <div class="card"><h3>Goals Set</h3><p>{{ data|map(attribute='goal')|list|length }}</p></div>
        </div>

        <table>
            <tr><th>Username</th><th>Full Name</th><th>Age</th><th>Height</th><th>Weight</th><th>Goal</th><th>Action</th></tr>
            {% for username, user in data.items() %}
            <tr>
                <td>{{ user.username }}</td>
                <td>{{ user.full_name }}</td>
                <td>{{ user.age }}</td>
                <td>{{ user.height_cm }}</td>
                <td>{{ user.weight_kg }}</td>
                <td>{{ user.goal }}</td>
                <td>
                    <form action="/delete" method="post" style="display:inline;">
                        <input type="hidden" name="username" value="{{ username }}">
                        <button type="submit" class="button">Delete</button>
                    </form>
                </td>
            </tr>
            {% endfor %}
        </table>

        <form action="/export/pdf" method="get">
            <button type="submit" class="button export-btn">Export to PDF</button>
        </form>
        <form action="/export/word" method="get">
            <button type="submit" class="button export-btn">Export to Word</button>
        </form>
    </div>
</body>
</html>
"""

    return render_template_string(html, data=data)

@app.route("/delete", methods=["POST"])
def delete_data():
    username = request.form["username"]
    with open("data.json", "r") as f:
        data = json.load(f)
    if username in data:
        del data[username]
        with open("data.json", "w") as f:
            json.dump(data, f)
    return show_data()

@app.route("/export/pdf")
def export_pdf():
    with open("data.json", "r") as f:
        data = json.load(f)
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["Username", "Full Name", "Age", "Height (cm)", "Weight (kg)", "Goal"]]
    for user in data.values():
        table_data.append([user["username"], user["full_name"], user["age"], user["height_cm"], user["weight_kg"], user["goal"]])
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.yellow),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.navy),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.orange),
    ]))
    doc.build([table])
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="fitness_data.pdf", mimetype="application/pdf")

@app.route("/export/word")
def export_word():
    with open("data.json", "r") as f:
        data = json.load(f)
    doc = Document()
    table = doc.add_table(rows=1, cols=6)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "Username"
    hdr_cells[1].text = "Full Name"
    hdr_cells[2].text = "Age"
    hdr_cells[3].text = "Height (cm)"
    hdr_cells[4].text = "Weight (kg)"
    hdr_cells[5].text = "Goal"
    for user in data.values():
        row_cells = table.add_row().cells
        row_cells[0].text = str(user["username"])
        row_cells[1].text = str(user["full_name"])
        row_cells[2].text = str(user["age"])
        row_cells[3].text = str(user["height_cm"])
        row_cells[4].text = str(user["weight_kg"])
        row_cells[5].text = str(user["goal"])
    table.style = 'Table Grid'
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="fitness_data.docx", mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

if __name__ == "__main__":
    app.run(debug=True)

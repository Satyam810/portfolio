from flask import Flask, request, jsonify, Response, send_file
import os

app = Flask(__name__)

# Home Route
@app.route("/")
def index():
    return send_file("index.html")


# Contact API
@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({
            "success": False,
            "error": "All fields are required."
        }), 400

    # In production you would store in DB or send email
    print(f"[CONTACT] {name} <{email}>: {message}")

    return jsonify({
        "success": True,
        "message": "Message received successfully!"
    })


# Sitemap
@app.route("/sitemap.xml")
def sitemap():
    return Response(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        '<url>'
        '<loc>https://satyamkumar.dev/</loc>'
        '<changefreq>monthly</changefreq>'
        '<priority>1.0</priority>'
        '</url>'
        '</urlset>',
        mimetype="application/xml"
    )


# Robots
@app.route("/robots.txt")
def robots():
    return Response(
        "User-agent: *\n"
        "Allow: /\n"
        "Sitemap: https://satyamkumar.dev/sitemap.xml",
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(debug=True)
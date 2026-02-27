from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route("/")
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    return Response(content, mimetype="text/html; charset=utf-8")

@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json()
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()
    if not name or not email or not message:
        return jsonify({"success": False, "error": "All fields required."}), 400
    print(f"[CONTACT] {name} <{email}>: {message}")
    return jsonify({"success": True, "message": "Message received!"})

@app.route("/sitemap.xml")
def sitemap():
    return Response(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        '<url><loc>https://satyamkumar.dev/</loc><changefreq>monthly</changefreq><priority>1.0</priority></url>'
        '</urlset>',
        mimetype="application/xml"
    )

@app.route("/robots.txt")
def robots():
    return Response(
        "User-agent: *\nAllow: /\nSitemap: https://satyamkumar.dev/sitemap.xml",
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)

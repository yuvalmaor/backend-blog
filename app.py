from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = [
        {"id": 1, "title": "Introduction to Next.js", "content": "Learn the basics of Next.js with App Router.", "date": "2025-01-23"},
        {"id": 2, "title": "Building APIs with Flask", "content": "A guide to building RESTful APIs using Flask.", "date": "2025-01-22"},
        {"id": 3, "title": "Deploying on Kubernetes", "content": "Steps to deploy applications on a k3s cluster.", "date": "2025-01-21"},
    ]
    return jsonify(posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

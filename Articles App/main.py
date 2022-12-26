from flask import Flask, jsonify, request
from storage import all_articles, liked_articles, not_liked_articles

app = Flask(__name__)

@app.route("/get-article")
def get_movie():
    article_data = {
        "title": all_articles[12],
        "url": all_articles[11],
        "timestamp": all_articles[1] or "N/A",
        "id":all_articles[0],
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_movie():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not-liked-article", methods=["POST"])
def not_liked_movie():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()
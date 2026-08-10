@app.route("/track", methods=["POST"])
def track():
    data = request.get_json()
    counts = {}
    for key in data:          # attacker-controlled keys
        counts[key] = counts.get(key, 0) + 1
    return jsonify(counts)

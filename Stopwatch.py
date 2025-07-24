from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

start_time = None

@app.route('/')
def home():
    return render_template('index.html')  # Frontend HTML page

@app.route('/start')
def start():
    global start_time
    start_time = time.time()
    return jsonify({"status": "started"})

@app.route('/stop')
def stop():
    global start_time
    if start_time is None:
        return jsonify({"error": "Stopwatch not started"})
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    start_time = None  # Reset
    return jsonify({"minutes": minutes, "seconds": seconds})

if __name__ == '__main__':
    app.run(debug=True)


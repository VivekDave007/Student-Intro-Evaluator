from flask import Flask, render_template, request, jsonify
from scorer import evaluate_introduction
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.get_json()
        transcript = data.get('transcript', '')
        duration = int(data.get('duration', 52))
        
        if not transcript.strip():
            return jsonify({'error': 'Transcript cannot be empty'}), 400
        
        # Evaluate the transcript
        results = evaluate_introduction(transcript, duration)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


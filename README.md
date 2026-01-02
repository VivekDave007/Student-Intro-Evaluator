```markdown
# AI Student Introduction Evaluator

AI Student Introduction Evaluator is a web application that analyzes and scores a student's **self‑introduction** based on structure, clarity, timing, and sentiment as part of the Nirmaan Education Internship Case Study.[page:1]

## Features

- Web interface for entering or pasting a student introduction for evaluation.[page:1]  
- REST API endpoint (`/evaluate`) that accepts JSON input and returns a detailed evaluation report.[page:1]  
- Sentiment analysis using VADER and basic numeric scoring with NumPy.[page:1]  
- Production-ready setup using `gunicorn` and `Procfile`, suitable for Railway deployment.[page:1]

## Tech Stack

- **Language**: Python 3  
- **Framework**: Flask (backend web framework)[page:1]  
- **Libraries**: `vaderSentiment`, `numpy`, `gunicorn`[page:1]  
- **Deployment**: Configured for Railway with `Procfile` and `requirements.txt`.[page:1]

## Project Structure

```text
Student-Intro-Evaluator/
├─ static/                          # Static assets (CSS, JS, images)
├─ templates/                       # HTML templates for the UI
├─ app.py                           # Main Flask application
├─ scorer.py                        # Core evaluation and scoring logic
├─ requirements.txt                 # Python dependencies
├─ Procfile                         # Process definition for gunicorn
├─ sample_transcript.txt            # Example student introduction
├─ Testing Checklist - AI Student Introduction Evaluator
└─ COMPLETE CODE - AI Student Intro Evaluator.docx
```

- `app.py`: Exposes the web UI at `/` and JSON API at `/evaluate`.[page:1]  
- `scorer.py`: Implements the logic to evaluate the introduction and compute scores.[page:1]  
- Documents and sample transcript support testing and review of the application.[page:1]

## Getting Started

### Prerequisites

- Python 3.10+ installed  
- `pip` available in your environment

### Installation

```bash
# Clone the repository
git clone https://github.com/VivekDave007/Student-Intro-Evaluator.git
cd Student-Intro-Evaluator

# (Optional) create and activate a virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

`requirements.txt` includes Flask, gunicorn, vaderSentiment, and numpy.[page:1]

### Running Locally

```bash
python app.py
```

The application starts with debug mode enabled and listens on `0.0.0.0` at port `5000`.[page:1]  
Open `http://localhost:5000` in your browser to access the web interface.

## API Usage

### Endpoint

- **URL**: `/evaluate`  
- **Method**: `POST`  
- **Content-Type**: `application/json`[page:1]

### Request Body

```json
{
  "transcript": "Your full student introduction goes here.",
  "duration": 52
}
```

- `transcript` (string, required): The text of the student introduction.  
- `duration` (integer, optional): Duration in seconds; defaults to `52` if missing.[page:1]

If `transcript` is empty or only whitespace, the API returns HTTP 400 with an error message.[page:1]

### Example cURL

```bash
curl -X POST http://localhost:5000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "transcript": "Hi, my name is Aarav...",
    "duration": 45
  }'
```

The response is a JSON object with computed scores and feedback fields from the evaluation logic.[page:1]

## Deployment

The project is configured for deployment using `gunicorn` and can be hosted on Railway or similar platforms.[page:1]

### Procfile

```text
web: gunicorn app:app
```

Basic Railway steps:

1. Push the repository to GitHub.  
2. Create a new project on Railway and connect this GitHub repo.  
3. Railway builds the app using `requirements.txt` and `Procfile`.  
4. Deploy and use the generated URL to access the application.[page:1]

## Testing

- Use `sample_transcript.txt` as input to quickly verify evaluation behavior.[page:1]  
- Follow the checklist in `Testing Checklist - AI Student Introduction Evaluator` for systematic manual testing.[page:1]  
- Confirm:
  - Empty transcripts return HTTP 400 with a clear error.  
  - Valid transcripts return a structured JSON with all expected scoring fields.[page:1]

## Future Enhancements

- Add authentication and a dashboard for teachers or evaluators.  
- Persist evaluation history in a database (SQLite/PostgreSQL).  
- Integrate speech-to-text to support audio introductions.  
- Improve the rubric with more advanced NLP models and configurable weighting.[page:1]
```

[1](https://github.com/VivekDave007/Student-Intro-Evaluator)

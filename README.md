# 🎌 Anime Recommendation API (FastAPI)

This project is a simple **anime recommendation engine** built using:

- `FastAPI` for API development
- `pandas` + `scikit-learn` (TF-IDF + cosine similarity) for content-based recommendations

You can send a search query (e.g., `"dark fantasy revenge"`) and get back a list of similar anime based on genre, title, and type.

---

## 🚀 Features

- 📡 REST API with `/recommend` POST endpoint
- 🧠 TF-IDF based semantic search
- 📊 Uses your own local anime CSV file
- ⚡ Fast response via Uvicorn server
- 🧪 Testable using Postman or `curl`

---

## 📁 Project Structure

```
travel_recommendation_system/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI routes
│   └── recommender.py       # TF-IDF + similarity logic
├── anime.csv                # Dataset (place it here or in /data)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Example Query

**POST** `/recommend`

**JSON Body:**

```json
{
  "query": "dark fantasy revenge",
  "top_n": 5
}
```

**Response:**

```json
[
  {
    "name": "Attack on Titan",
    "genre": "Action, Drama, Fantasy",
    "type": "TV",
    "rating": 8.8
  },
  ...
]
```

## 🛠️ Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/your-username/anime-recommender-fastapi.git
cd anime-recommender-fastapi
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your dataset

Place `anime.csv` in the root or update the path inside `recommender.py`.

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

Now open your browser at:

- 👉 `http://127.0.0.1:8000/docs` (Swagger UI)
- 👉 `http://127.0.0.1:8000/recommend` (for POST requests)

## 📦 Requirements

```
fastapi
uvicorn
pandas
numpy
scikit-learn
```

Install using: `pip install -r requirements.txt`

## 🧪 Test with Postman or Curl

```bash
curl -X POST http://127.0.0.1:8000/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "space adventure", "top_n": 5}'
```

## 🧰 Future Plans

- Add support for filtering by type (TV, OVA, Movie)
- Allow rating thresholds
- Add sorting by similarity
- Host on Render or Railway
- Frontend using Next.js

## 📝 License

MIT License. Use, remix, and share.

## 🙏 Credits

- FastAPI
- scikit-learn
- Original Anime Dataset

---

## ✅ Final Tip

Save it as `README.md` in your root directory. You can preview it locally using VS Code Markdown Preview (`Ctrl+Shift+V`).

Want a logo, badges (build passing, license, etc.), or to turn this into a public web service? I can prep that too.

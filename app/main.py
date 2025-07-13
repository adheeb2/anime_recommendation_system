from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from recommender import recommend_anime

app = FastAPI()

class RecommendRequest(BaseModel):
    query:str
    top_n:int = 5

@app.post('/recommend')
def recommend(request:RecommendRequest):
    results = recommend_anime(request.query,request.top_n)
    if results.empty:
        raise HTTPException(status_code=404,detail="no result found, try different keywords")
    return results.to_dict(orient="records")
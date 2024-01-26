from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_summary(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful, pattern-following assistant that summarizes historical content into easy to understand, bite-sized pieces."},
            {"role": "user", "content": text}
        ],
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )

    summary = response.choices[0].message.content
    cleaned_summary = summary.replace('\n', '').replace('\n\n', ' ')
    return cleaned_summary

@app.get("/")
def home():
    return {"message": "Welcome to the Text Summarizer API"}

@app.post("/summarize/")
def summarize_text(data: dict):
    text = data.get("text", "")
    summary = generate_summary(text)
    return {"summary": summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

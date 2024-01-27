# Text Summarizer App

Welcome to the Text Summarizer App! This application allows you to generate summaries for text using OpenAI's GPT-3.5 Turbo model.

## Features

- **Simple Interface**: Easily enter the text you want to summarize in the provided textarea.
- **Quick Summarization**: Click the "Summarize" button to generate a concise summary.

## Getting Started

1. Clone the repository to your local machine.
2. Set up your OpenAI API key in the environment variable `OPENAI_API_KEY`.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the FastAPI backend using `uvicorn main:app --reload`.
5. Run the Vite/React frontend using `npm install npm run dev`.
6. Navigate to `http://localhost:5173/` to access the app. 

## Technologies Used

- FastAPI for the backend server.
- React for the frontend user interface.
- OpenAI GPT-3.5 Turbo for text summarization.

![Text Summarizer App](https://i.imgur.com/WyUFFpB.png)


**Note:** Ensure you have the necessary permissions and adhere to OpenAI's terms of service when using the GPT-3.5 Turbo model.

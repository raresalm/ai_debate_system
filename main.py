import ollama
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Connection to your local Ollama engine
client = ollama.Client(host='http://host.docker.internal:11434')

def ask_ai(model_name, prompt):
    try:
        response = client.chat(model=model_name, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "step": "start"})

@app.post("/debate", response_class=HTMLResponse)
async def debate_step(
    request: Request, 
    topic: str = Form(None), 
    pro_speech: str = Form(""), 
    con_speech: str = Form(""),
    step: str = Form("start")
):
    # STEP 1: Pro Opening
    if step == "start":
        pro_speech = ask_ai("llama3", f"Team PRO. Topic: {topic}. Give a strong 3-sentence opening.")
        next_step = "pro_done"
        
    # STEP 2: Con Counter
    elif step == "pro_done":
        con_speech = ask_ai("mistral", f"Team CON. Topic: {topic}. Pro said: {pro_speech}. Give a 3-sentence rebuttal.")
        next_step = "con_done"
        
    # STEP 3: Judge Verdict
    elif step == "con_done":
        verdict_prompt = f"Topic: {topic}\nPro Argument: {pro_speech}\nCon Argument: {con_speech}\nWho won and why? (2 sentences)"
        verdict = ask_ai("phi3", verdict_prompt)
        return templates.TemplateResponse("index.html", {
            "request": request, "topic": topic, "pro_speech": pro_speech, 
            "con_speech": con_speech, "verdict": verdict, "step": "finished"
        })

    return templates.TemplateResponse("index.html", {
        "request": request, "topic": topic, "pro_speech": pro_speech, 
        "con_speech": con_speech, "step": next_step
    })
import requests 
import gradio as gr

# function

def chat(message, history):
    r = requests.post("http://localhost:11434/api/generate",
                      json={
                          "model": "qwen2.5:7b",
                          "prompt": message,
                          "stream" : False
                      })
    return r.json()["response"]
gr.ChatInterface(chat).launch()
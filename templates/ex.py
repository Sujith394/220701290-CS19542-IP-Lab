import google.generativeai as genai
genai.configure(api_key='AIzaSyAprunPJ7iQ_nFtBK8wTd9L2S0qRXkzh_8')
generation_config={
    "temperature":0.9,
    "top_p":1,
    "top_k":1,
    "max_output_tokens": 2048,

}

available_models = genai.list_models()
print(available_models)
model= genai.GenerativeModel(model_name="models/gemini-1.5-pro",
                             generation_config=generation_config
                             )
convo=model.start_chat(history=[])
convo.send_message("create a iternary trip plan for 3 days from chennai to kerala")
print(convo.last.text)
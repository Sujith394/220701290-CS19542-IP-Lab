import google.generativeai as genai
genai.configure(api_key='AIzaSyAprunPJ7iQ_nFtBK8wTd9L2S0qRXkzh_8')
generation_config={
    "temperature":0.9,
    "top_p":1,
    "top_k":1,
    "max_output_tokens": 2048,

}
model= genai.GenerativeModel(model_name="models/gemini-1.5-pro",
                             generation_config=generation_config
                             )
convo=model.start_chat(history=[])
def generate_itinerary(source, destination, start_date, end_date, no_of_day):
    prompt = f"Generate a personalized trip itinerary for a {no_of_day}-day trip {source} to {destination} from {start_date} to {end_date}, with an optimum budget (Currency:INR)."
    convo.send_message(prompt)
    
    return(convo.last.text)
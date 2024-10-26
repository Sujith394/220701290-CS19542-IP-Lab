import google.generativeai as genai

# Replace with your valid API key
api_key = 'AIzaSyAprunPJ7iQ_nFtBK8wTd9L2S0qRXkzh_8'
genai.configure(api_key=api_key)

available_models = genai.list_models()

for model in available_models:
  print(f"Model Name: {model.name}")
 
  print("-" * 50)

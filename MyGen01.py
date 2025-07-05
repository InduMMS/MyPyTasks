import google.generativeai as genai

genai.configure(api_key="AIzaSyDwVB2bSJXH_DAUZfr5m5_XdVOrEKxAR0E")

model = genai.GenerativeModel('gemini-2.5-flash')

response = model.generate_content(contents="How can a 57 year old Software engineer get a job with basic python skills in INDIA Hyderabad. He graduated from BITS Pilani. He has MBA, MCA. He worked in US as a software consultant for 10 years")
print(response.text)



"""


model = genai.GenerativeModel(model_name="models/veo")
prompt = "Swamy Vivekananada and Brahmanandam"
response = model.generate_content(prompt)







for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
"""
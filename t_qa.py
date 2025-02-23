import json
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "mistralai/Mistral-7B-v0.3"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Sample data
trail_data = [
    {
        "name": "UTMB",
        "start": "Chamonix",
        "end": "Chamonix",
        "distance": "171 km",
        "elevation_gain": "10,000 m",
        "average_time": "40 hours",
        "best_time": "19 hours 49 minutes",
        "max_time": "46 hours 30 minutes",
        "profile": "Mountainous with steep ascents and descents"
    },
    {
        "name": "Western States 100",
        "start": "Olympic Valley, CA",
        "end": "Auburn, CA",
        "distance": "100 miles",
        "elevation_gain": "18,000 ft",
        "average_time": "24 hours",
        "best_time": "14 hours 46 minutes",
        "max_time": "30 hours",
        "profile": "Varied terrain with significant elevation changes"
    }
]

# Function to preprocess the data
def preprocess_data(data):
    """
    Preprocess the trail race data into a format suitable for the model.
    """
    processed_data = []
    for race in data:
        processed_race = (
            f"Name: {race['name']}\nStart: {race['start']}\nEnd: {race['end']}\n"
            f"Distance: {race['distance']}\nElevation Gain: {race['elevation_gain']}\n"
            f"Average Time: {race['average_time']}\nBest Time: {race['best_time']}\n"
            f"Max Time: {race['max_time']}\nProfile: {race['profile']}"
        )
        processed_data.append(processed_race)
    return processed_data

# Preprocess the data
processed_trail_data = preprocess_data(trail_data)

# Aswer questions using the model
def answer_question(question, context):
    """
    Answer a question using the model and the provided context.
    """
    inputs = tokenizer(f"Context: {context}\nQuestion: {question}\nAnswer:", return_tensors="pt")
    outputs = model.generate(**inputs)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

# Find the relevant context for a question
def find_relevant_context(question, data):
    """
    Find the relevant context for a question from the preprocessed data.
    """
    # Simple keyword matching for demonstration purposes
    keywords = question.lower().split()
    for context in data:
        if all(keyword in context.lower() for keyword in keywords):
            return context
    return None

question = "What is the distance of the UTMB?"

# Find the relevant context for the question
relevant_context = find_relevant_context(question, processed_trail_data)

if relevant_context:
    answer = answer_question(question, relevant_context)
    print(answer)
else:
    print("No relevant context found for the question.")

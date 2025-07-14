import gradio as gr
import random
import json

  # --- Load Real CBSE Content from JSON File ---
def load_cbse_data(subject):
      try:
          with open(f"data/class6_{subject.lower()}.json", "r", encoding="utf-8") as f:
              return json.load(f)
      except FileNotFoundError:
          return None

current_subject = "science"
data = load_cbse_data(current_subject)

  # --- Core Logic # ---  
def get_random_mcq():
    if not data or "mcqs" not in data:
        return "No data found for subject.", [], ""
    mcq = random.choice(data["mcqs"])
    question = mcq["question"]
    options = mcq["options"]
    answer = mcq["answer"]
    return question, options, answer

def quiz_mode(user_input, state):
      if not state:
          q, opts, ans = get_random_mcq()
          if isinstance(q, str):  # handle error case
              return q, None
          state = {"question": q, "options": opts, "answer": ans}
          options_display = "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(opts)])
          return f"Q: {q}\n\n{options_display}\n\nReply with option number.", state
      else:
          correct = state["answer"]
          try:
              selected_index = int(user_input.strip()) - 1
              selected = state["options"][selected_index]
              if selected == correct:
                  msg = "✅ Correct!"
              else:
                  msg = f"❌ Incorrect. Correct answer is: {correct}"
          except:
              msg = "❌ Invalid input. Please enter a valid option number."
          state = None
          return msg + "\n\nType 'quiz' to try another.", state

def chatbot_response(message, state):
      if message.lower().startswith("subject:"):
          global current_subject, data
          current_subject = message.split(":")[1].strip().lower()
          data = load_cbse_data(current_subject)
          if data:
            return f"✅ Subject switched to {current_subject.capitalize()}. Type 'quiz' to begin.", None
          else:
            return f"❌ Data not found for subject: {current_subject}", None
      elif message.lower() == "quiz":
          return quiz_mode(None, None)
      elif state:
        return quiz_mode(message, state)
      else:
        return "I'm a CBSE Class 6 assistant. Type 'quiz' to begin a quiz, or 'subject:maths' to switch subject.", None

chatbot = gr.ChatInterface(fn=chatbot_response, 
                           title="CBSE Class 6 Learning Assistant",
                           description="Type 'quiz' to start a quiz or 'subject:science', 'subject:social' to change subject.")

chatbot.launch()                                                                                 


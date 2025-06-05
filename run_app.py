import streamlit as st
import joblib

# Load model + vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("🌾 မြန်မာစိုက်ပျိုးရေး Chatbot 🌱")

# Define keyword-based clarifications
clarification_map = {
    "စပါး": """စပါးနှင့်ပတ်သက်လို့ဘာများသိချင်ပါသလဲ?

၁။ စပါးမိတ်ဆက်  
၂။ စပါးစိုက်စနစ်  
၃။ စပါးမျိုးကွဲများ  
၄။ စပါးတွင်ကျရောက်တတ်သောအင်းဆက်ပိုးများ  
၅။ စပါးတွင်ကျရောက်တက်သောရောဂါများ  
၆။ စပါးတွင်ကျရောက်တတ်သောပေါင်းပင်များ  
""",
    "သစ်ခွ": """သစ်ခွနှင့်ပတ်သက်၍ မေးခွန်းတစ်ခုရွေးပါ:

၁။ သစ်ခွစိုက်ပျိုးနည်း  
၂။ သစ်ခွရောဂါများ  
၃။ သင့်တော်သောမြေဓာတ်
""",
    # Add other keywords if needed...
}

# Detect if the input is a top-level keyword
def is_keyword_input(text):
    return text.strip() in clarification_map

def get_answer(question):
    X = vectorizer.transform([question])
    answer = model.predict(X)[0]
    return answer

user_input = st.text_input("မေးခွန်းထည့်ပါ...")

if user_input:
    if is_keyword_input(user_input):
        st.markdown(f"🤖 **{clarification_map[user_input.strip()]}**")
    else:
        try:
            response = get_answer(user_input)
            st.markdown(f"🤖 **ဖြေချက်**: {response}")
        except Exception as e:
            st.error("စိတ်မရှိပါနဲ့၊ မေးခွန်းကိုနားမလည်နိုင်ပါ။")
# 🌾 Agriculture Chatbot System

A Python-based conversational chatbot built to assist farmers, students, and agricultural researchers by answering agriculture-related queries using **Natural Language Processing (NLP)**. The system uses **TF-IDF vectorization** and **NLTK** to process and respond to user input based on a predefined knowledge base.

---

## 🧠 Technologies & Libraries Used

- **Programming Language**: Python 3.x
- **NLP Libraries**:
  - `NLTK` (Natural Language Toolkit)
  - `sklearn.feature_extraction.text.TfidfVectorizer`
  - `sklearn.metrics.pairwise.cosine_similarity`
- **Preprocessing**:
  - Tokenization, Lemmatization, Stopword Removal
- **Other**:
  - Basic command-line interface (CLI)
  - Text file for knowledge base (FAQs)

---

## 📋 Features

- 👨‍🌾 Responds to common agriculture-related questions
- 📚 Uses TF-IDF to vectorize user input and match with the most relevant question
- 🔍 Cosine similarity to measure semantic closeness between input and knowledge base
- ✂️ Preprocessing: Lowercasing, punctuation removal, stopword filtering, lemmatization
- 🧾 Easily extensible FAQ dataset

---

## ⚙️ How It Works

1. User types a question related to agriculture.
2. System processes the input using NLTK (tokenization, lemmatization, etc.).
3. TF-IDF is used to vectorize both the user input and the stored questions.
4. Cosine similarity measures how close the input is to stored questions.
5. The chatbot returns the most relevant answer.

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/agriculture-chatbot.git
cd agriculture-chatbot
````

### 2. Set up Python environment

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`**

```
nltk
scikit-learn
```

### 4. Download NLTK Data (Only once)

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
```

---

## 🧪 Example Usage

```bash
python chatbot.py
```

**User Input:**

```
စပါးတွင်ကျရောက်တတ်သောအင်းဆက်ပိုးများ၊ သစ်ခွ စိုက်ပျိုးရာတွင် အရေးကြီးသောအချက်များ ဘာတွေလဲ?
```

**Bot Response:**

```
စပါးတွင်အောက်ပါအင်းဆက်ပိုးများကျရောက်တတ်ပါသည် -
(၁)စပါးလောင်မီးပိုး
(၂)စပါးရွက်လိပ်အိမ်ပိုး
(၃)စပါးငမြှောင်တောင်ပိုး
(၄)စပါးဆစ်ပိုး
(၅)စပါးကြက်သွန်မြိတ်ပိုး
(၆)စပါးသရစ်ပိုး
(၇)စပါးဖြုတ်ပိုး
(၈)စပါးနှံစုပ်ပိုး
(၉)စပါးနှံဖြတ်ပိုး
(၁၀)စပါးရွက်လိပ်ရွက်ခေါက်ပိုး
(၁၁)စပါးရွက်စားယင် (ရွက်ဗွေလောက်)
(၁၂)စပါးဖြုတ်ညိုပိုး'),
(5, 'စပါးတွင်အောက်ပါရောဂါများကျရောက်တတ်ပါသည် -
(၁)စပါးဂုတ်ကျိုးရောဂါ
(၂)စပါးရွက်ဖုံးပုပ်ရောဂါ
(၃)စပါးရွက်ဖုံးခြောက်ရောဂါ
(၄)စပါးရွက်ညိုပြောက်ရောဂါ
(၅)စပါးရွက်ညိုပြောက်ရှည်ရောဂါ
(၆)စပါးမှိုသီးရောဂါ
(၇)စပါးပင်စည်ပုပ်ရောဂါ
(၈)စပါးပင်ရှည်ရောဂါ၊ပျိုးပင်နာကျရောဂါ
(၉)စပါးဘက်တီးရီးယားရွက်ခြောက်ရောဂါ
(၁၀)စပါးဘက်တီးရီးယားရွက်စင်းရောဂါ
(၁၁)စပါးဘက်တီးရီးယား ပင်ခြေပုပ်ရောဂါ
(၁၂)စပါးယူဖရာရောဂါ(သို့)စပါးလောင်မီးရောဂါ
(၁၃)စပါးရွက်ဖျားဖြူ ရောဂါ
(၁၄)စပါးမြစ်ဖုရောဂါ

သစ်ခွစိုက်ပျိုးရာတွင် မြေညီပြင်ဆင်ခြင်း၊ ရေချိန်ညှိခြင်း အရေးကြီးပါသည်။
```

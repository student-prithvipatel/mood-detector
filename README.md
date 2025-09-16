# Mood Detector by Text AI 🎭

A simple **AI-powered app** that detects the mood from text input using NLP.  
Built with **Python, Streamlit, and Hugging Face Transformers**.  

---

### 🚀 Features
- Enter any text (sentence/paragraph).
- AI predicts emotions like *joy, sadness, anger, love, surprise, fear, disgust, neutral*.
- Shows the **top emotion** with confidence, emoji, and color.
- Displays **all emotions in a bar chart** for better visualization.

---

### 🛠️ Tech Stack
- **Python 3.11**
- **Streamlit**
- **Transformers (Hugging Face)**
- **PyTorch**
- **Pandas & Altair** (for visualization)

---

### 📦 Installation
```bash
# Clone the repo
git clone https://github.com/your-username/mood-detector.git
cd mood-detector

# Install dependencies
pip install -r requirements.txt
```

---

### ▶️ Run the App
```bash
streamlit run app.py
```

---

### ✨ Example
Input:
```bash
I just got a new job and I’m super excited!
```

Output:
```bash
Mood Detected: Joy 😄 (Confidence: 0.95)
```
Plus, a bar chart showing probabilities of all emotions.

---

### 📌 Future Improvements
- Train a custom mood classification model.
- Add emoji-based responses for each mood.
- Deploy on Streamlit Cloud or Hugging Face Spaces.

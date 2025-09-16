import streamlit as st
from transformers import pipeline
import pandas as pd
import altair as alt

# Load multi-emotion model
classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

# Streamlit UI
st.set_page_config(page_title="Mood Detector", page_icon="😊")
st.title("✨ Advanced Mood Detector ✨")
st.write("Type your text below and see your mood!")

# Input box
user_input = st.text_area("Enter text here:")

if st.button("Detect Mood"):
    if user_input.strip() != "":
        results = classifier(user_input)[0]  # List of emotions with scores

        # Find emotion with highest score
        top_emotion = max(results, key=lambda x: x['score'])
        label = top_emotion['label']
        score = top_emotion['score']

        # Emoji & color mapping
        mood_map = {
            "joy": ("😄", "green"),
            "sadness": ("😢", "blue"),
            "anger": ("😡", "red"),
            "fear": ("😨", "purple"),
            "surprise": ("😲", "orange"),
            "love": ("😍", "pink"),
            "disgust": ("🤢", "brown"),
            "neutral": ("😐", "gray")
        }

        emoji, color = mood_map.get(label, ("❓", "black"))
        st.markdown(
            f"<h2 style='color:{color}'>Mood Detected: {label.capitalize()} {emoji} "
            f"(Confidence: {score:.2f})</h2>",
            unsafe_allow_html=True
        )

        # 📊 Show all scores in a bar chart
        df = pd.DataFrame(results)
        chart = alt.Chart(df).mark_bar().encode(
            x="label",
            y="score",
            color="label"
        )
        st.altair_chart(chart, use_container_width=True)

    else:
        st.warning("⚠️ Please enter some text!")

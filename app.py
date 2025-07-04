import streamlit as st
import joblib
import pandas as pd

# --------------------------------------------
# Comment Sentiment Analyzer App
# --------------------------------------------
st.set_page_config(
    page_title="Comment Analyzer",
    page_icon="💬",
    layout="centered"
)

# --------------------------------------------
# Heading
# --------------------------------------------
st.markdown("<h1 style='text-align: center; color: #FF4500;'>💬 Comment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analyze the sentiment of Reddit comments quickly and easily! 🔍</p>", unsafe_allow_html=True)

# --------------------------------------------
# Input Text Area
# --------------------------------------------
comment = st.text_area("💬 Enter Comment", placeholder="Type or paste the Reddit comment here...", height=150)

# --------------------------------------------
# Load Pretrained Model
# --------------------------------------------
try:
    model = joblib.load('./Models/Model.pkl')  
except Exception as e:
    st.error("❌ Failed to load the model. Check the file path and model compatibility.")
    st.stop()

# --------------------------------------------
# Predict Button and Sentiment Analysis
# --------------------------------------------
if st.button("🔍 Predict"):
    if comment.strip() == "":
        st.warning("⚠️ Please enter a comment before predicting.")
    else:
        with st.spinner("Analyzing sentiment..."):
            prediction = model.predict([comment])[0]
            probabilities = model.predict_proba([comment])[0]

            class_index = list(model.classes_).index(prediction)
            confidence = probabilities[class_index] * 100

            emoji_map = {
                "Negative": "☹️",
                "Neutral": "😐",
                "Positive": "😊"
            }
            color_map = {
                "Negative": "#FF6B6B",
                "Neutral": "#FFD93D",
                "Positive": "#6BCB77"
            }

            sentiment_label = f"{emoji_map.get(prediction, '')} {prediction}"

            st.markdown(
                f"""
                <div style="
                    background-color: {color_map.get(prediction, '#eee')};
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    color: white;
                    font-size: 24px;
                    font-weight: bold;">
                    {sentiment_label}
                </div>
                """, unsafe_allow_html=True
            )
            st.progress(min(int(confidence), 100))
            st.markdown(f"**Confidence:** {confidence:.2f}%")

            prob_df = pd.DataFrame({
                "Sentiment": model.classes_,
                "Probability": probabilities
            })

            st.markdown("### Class Probabilities")
            st.bar_chart(prob_df.set_index("Sentiment"))

            st.write(prob_df.style.format({"Probability": "{:.2%}"}))

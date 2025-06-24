
import streamlit as st
import pandas as pd

# Load translation data
df = pd.read_excel("indigenous_translation_phrases_cleaned.xlsx")

# Theme toggle
theme = st.sidebar.radio("Choose Theme", ["🌞 Light Mode", "🌙 Dark Mode"])
if theme == "🌙 Dark Mode":
    st.markdown("<style>body { background-color: #1e1e1e; color: white; }</style>", unsafe_allow_html=True)

# Header
st.set_page_config(page_title="PharmaLingua Chatbot", layout="centered")
st.markdown("<h1 style='text-align: center;'>💬 PharmaLingua Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Empowering Nigerian pharmacists with indigenous language support</p>", unsafe_allow_html=True)

# Language & Direction
col1, col2 = st.columns([2, 2])
with col1:
    language = st.selectbox("Choose Language", ["Berom", "Afizere", "Mwaghavul"])
with col2:
    direction = st.selectbox("Translate Direction", ["English → Indigenous", "Indigenous → English"])

# Input Area with Suggestions
if direction == "English → Indigenous":
    phrase_options = df["english"].dropna().unique().tolist()
else:
    phrase_options = df[language.lower()].dropna().unique().tolist()

user_input = st.selectbox("💡 Select or type a phrase", [""] + phrase_options)
st.button("🎤 Speak to Chatbot (Coming Soon)", disabled=True)
st.button("🔊 Read Translation Aloud (Coming Soon)", disabled=True)

# Translate
if st.button("🔍 Translate"):
    if user_input.strip() == "":
        st.warning("Please enter or select a phrase.")
    else:
        if direction == "English → Indigenous":
            match = df[df['english'].str.lower() == user_input.lower()]
            if not match.empty:
                result = match[language.lower()].values[0]
                if pd.isna(result) or result.strip() == "":
                    st.info(f"No translation available in {language}.")
                else:
                    st.success(f"**Translation in {language}:**\n\n{result}")
            else:
                st.error("Phrase not found in English list.")
        else:
            match = df[df[language.lower()].str.lower() == user_input.lower()]
            if not match.empty:
                result = match["english"].values[0]
                st.success(f"**Translation in English:**\n\n{result}")
            else:
                st.error("Phrase not found in selected language.")

# Additional mock features
with st.expander("🔧 Future Features (Coming Soon)"):
    st.button("📜 View Chat History")
    st.button("📥 Download Conversation Log")
    st.button("📍 Use My Location to Auto-Select Language")
    st.button("🧠 Suggest Related Phrases")
    st.button("👤 Switch to 'Patient Mode'")

# CTA Section
st.markdown("---")
st.subheader("🌍 Join Our Mission")
st.markdown("Would you like to help us improve language support in healthcare? Join our volunteer network or submit new translations!")

with st.form("join_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")
    message = st.text_area("Message / Languages you can help with")
    if st.form_submit_button("Join Our Team"):
        st.success("Thank you! We’ll reach out to you soon.")

# Rating
st.markdown("---")
st.subheader("⭐ Rate PharmaLingua")
rating = st.slider("How would you rate this prototype?", 1, 5, 3)
if st.button("Submit Rating"):
    st.success(f"Thanks for rating us {rating} out of 5!")

# Footer
st.markdown("---")
st.caption("🚀 Built for the Hackathon: *Nigerian Pharmacists in the AI Lab*")

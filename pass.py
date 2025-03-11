import streamlit as st
import re

# Function to calculate password strength
def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) < 6:
        remarks.append("Too short (Minimum 6 characters).")
    elif len(password) >= 8:
        strength += 1
        remarks.append("Good length.")

    if re.search(r"[a-z]", password):
        strength += 1
        remarks.append("Contains lowercase letter.")
    else:
        remarks.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
        remarks.append("Contains uppercase letter.")
    else:
        remarks.append("Add uppercase letters.")

    if re.search(r"\d", password):
        strength += 1
        remarks.append("Contains digits.")
    else:
        remarks.append("Add digits.")

    if re.search(r"[^A-Za-z0-9]", password):
        strength += 1
        remarks.append("Contains special characters.")
    else:
        remarks.append("Add special characters (!, @, #, etc).")

    # Determine strength level
    if strength <= 2:
        level = "Weak"
        color = "red"
    elif strength == 3 or strength == 4:
        level = "Moderate"
        color = "orange"
    else:
        level = "Strong"
        color = "green"

    return level, color, remarks

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    level, color, remarks = check_password_strength(password)

    st.markdown(f"**Strength Level:** :{color}[{level}]")
    progress = {"Weak": 0.3, "Moderate": 0.6, "Strong": 1.0}
    st.progress(progress[level])

    st.subheader("Suggestions / Feedback:")
    for remark in remarks:
        st.write(f"- {remark}")

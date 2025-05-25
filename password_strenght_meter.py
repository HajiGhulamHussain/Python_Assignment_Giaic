import streamlit as st
import re

st.set_page_config(page_title="Password strenght Checker", page_icon="🔐")
st.title("Password Strength Checker 🔐")

st.markdown("""
This app checks the strength of your password based on various criteria
            use this to ensure your password is secure and robust.
A strong password should contain at least 8 characters, including:
            **Strong Password**:""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
        feedback.append("✅ At least 8 characters")
    else:
        feedback.append("❌ Less than 8 characters ")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Password Contains both uppercase and lowercase letters")
    else:
        feedback.append("❌ Missing uppercase or lowercase letters A-Z, a-z")

    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("✅ Password Contains numbers")
    else:
        feedback.append("❌ Missing numbers in password (0-9)")

    if re.search(r"[!@#$%^&]", password):
        score += 1
        feedback.append("✅ Password Contains special characters")
    else:
        feedback.append("❌ Missing special characters in password (!@#$%^&)")

    if score == 4:
        st.success("Your password is strong! 💪")

    elif score == 3:
        st.warning("Your password is moderate. Consider adding more complexity. ⚠️")
    else:
        st.error("Your password is weak. Please improve it! ❌")

    if feedback:
        st.markdown("### Improvedment suggestion:")
    for tip in feedback:
        st.markdown(tip)
else:
    st.info("Please enter a password to check its strength.") 




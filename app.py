#password strength..
import streamlit as st
import re
st.set_page_config(page_title="Password Strenght Checker", page_icon="0")

st.title("Password Strenght Checker")
st.markdown("""
Welcone to the ultimate Password Strenght Checker!
Use This Simple Tool To Check The Strenght Of Your Password
$ get Suggestions On How To Make It Stronger.
   We Will Give You Helpfull Tips To Create A **STRONG PASSWORD**""")

Password = st.text_input("Enter your password", type="password")
feedback=[ ]
score = 0

if Password :
    if len(Password)>=8:
        score+=1
    else:
        feedback.append("Password should be atleast 8 characters long.")
    if re.search(r"[A-Z]",Password) and re.search(r"[a-z]",Password):
     score+=1
    else:
        feedback.append("Password should contain both upper and lower case characters.")
    if re.search(r'\d', Password):
     score+=1
    else:
        feedback.append("Password should contain at least one digit.")
    if re.search(r'[!@$%&]', Password):
     score+=1
    else:
        feedback.append("Password should contain atlease one special characters (!@$%&).")
    if score == 4:
     feedback.append("Your password is strong.")
    elif score ==3:
     feedback.append("Your password is medium strenght. It could be stronger")
    else:
     feedback.append("Your password is weak. Please make it stronger.")
    
    if feedback:
     st.markdown('##Improvement Suggestion')
    for tip in feedback:
        st.write(tip)
else:
    st.info("Please enter your password to get started.")

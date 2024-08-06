import streamlit as st

encrypt = {
    "a": "z",
    "b": "y",
    "c": "x",
    "d": "w",
    "e": "v",
    "f": "u",
    "g": "t",
    "h": "s",
    "i": "r",
    "j": "q",
    "k": "p",
    "l": "o",
    "m": "n",
    "n": "m",
    "o": "l",
    "p": "k",
    "q": "j",
    "r": "i",
    "s": "h",
    "t": "g",
    "u": "f",
    "v": "e",
    "w": "d",
    "x": "c",
    "y": "b",
    "z": "a",
}

st.set_page_config(page_title="Cryptography", page_icon="🔐", layout="wide")
st.title("Cryptography")
st.write("This is a simple web app that allows you to encrypt and decrypt text.")
op=st.text_area("Enter the text you would like to encrypt here:", height=10)

op=op.lower()
length=len(op)
encrypted = ''
if st.button("Encrypt"):
    for char in op:
        
        if char in encrypt:
            encrypted = encrypted + encrypt[char]
        else:
            encrypted = encrypted + char
         
    st.write("The encrypted code is: "+encrypted)
    st.write("ENCRYPTION COMPLETE")
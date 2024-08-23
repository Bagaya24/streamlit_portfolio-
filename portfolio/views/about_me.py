import re

import requests
import streamlit as st


# -- fonction --- #
@st.dialog("Contact me")
def show_contact_form():
    WEBHOOK_URL = ""
    def is_valid_email(email):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+$"
        return re.match(email_pattern, email) is not None

    with st.form("Contact_form"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prenom")
        mail = st.text_input("Email")
        message = st.text_area("Message")
        btn_submit = st.form_submit_button("Soumettre")

        if btn_submit:

            if not nom:
                st.error("Entre votre nom")
                st.stop()
            if not prenom:
                st.error("Entre votre prenom")
                st.stop()
            if not mail:
                st.error("Entre votre mail")
                st.stop()
            if not is_valid_email(mail):
                st.error("Entre un mail valide")
            if not message:
                st.error("Entre votre message")
                st.stop()
            data = {
                "email": mail,
                "nom": nom,
                "prenom": prenom,
                "message": message
            }
            response = requests.post(WEBHOOK_URL, json=data)
            if response.status_code == 200:
                st.success("Votre message a ete envoye!")
            else:
                st.error("Il y'a eu un probleme lors de l'envoi de votre message")


# --- hero section --- #

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("assets/WhatsApp Image 2024-03-31 à 11.23.43_914c86bb.jpg", width=250)
with col2:
    st.title("John Do", anchor=False)
    st.write(
        "Devellopeur python"
    )
    if st.button("💌 contact me"):
        show_contact_form()

st.write("\n")
st.subheader("Etudes et qualification", anchor=False)
st.write(
    """
    - Diplomer en Electronique au secondaire
    - 5 ans d'experience en installation des antennes canal plus
    - Formation complete en python
    """
)

st.write('\n')
st.subheader("Competences")
st.write(
    """
    - Programation: Python, flutter, SQL, C++, HTML, CSS, Arduino
    - Base de donnees: MySQL
    - Logiciel: Proteus, SolidWorks, MatLab
    """
)
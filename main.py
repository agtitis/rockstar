import streamlit as st

# Ρυθμίσεις σελίδας
st.set_page_config(page_title="Ποιος Rockstar είσαι;", page_icon="🎸", layout="centered")

# Χρώματα και γραμματοσειρές
tx_colour = "#ffffff"
bg_colour = "#b566ff"
font_type = "Verdana"

# Αρχικοποίηση μεταβλητών στο session state
if 'page' not in st.session_state:
    st.session_state.page = "intro"

# Συναρτήσεις αλλαγής σελίδας
def go_to_questions():
    st.session_state.page = "questions"

def go_to_end():
    st.session_state.page = "end"

# Σελίδες

# Intro Page
if st.session_state.page == "intro":
    st.markdown(
        f"<h1 style='text-align: center; color: {tx_colour}; background-color: {bg_colour}; "
        f"padding: 20px; font-family:{font_type};'>Ποιος Rockstar είσαι;</h1>",
        unsafe_allow_html=True
    )
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("guitarist.png", width=200)

    with col2:
        st.markdown(
            f"<div style='background-color:{bg_colour}; padding: 20px; border-radius: 10px;'>"
            f"<p style='color: {tx_colour}; font-family: {font_type}; font-size:16px;'>"
            f"Γεια σου. Θέλεις να μάθεις ποιο είναι το Rockstar όνομά σου;<br><br>"
            f"Κάνε κλικ στο κουμπί Έναρξη, απάντησε σε μερικές απλές ερωτήσεις και "
            f"θα σου αποκαλύψω το Rockstar όνομά σου!!"
            f"</p></div>",
            unsafe_allow_html=True
        )
        st.button("Έναρξη", on_click=go_to_questions)

# Questions Page
elif st.session_state.page == "questions":
    st.markdown(
        f"<h1 style='text-align: center; color: {tx_colour}; background-color: {bg_colour}; "
        f"padding: 20px; font-family:{font_type};'>Ερωτήσεις</h1>",
        unsafe_allow_html=True
    )

    with st.form(key='questions_form'):
        name = st.text_input("Όνομα")
        band = st.text_input("Ποιος είναι ο αγαπημένος σου καλλιτέχνης;")
        dob = st.text_input("Ποια είναι η ημερομηνία γέννησης;")
        pet = st.text_input("Ποια είναι η αγαπημένη σου ομάδα;")
        maiden = st.text_input("Ποιο είναι το αγαπημένο σου χρώμα;")
        submitted = st.form_submit_button("Υποβολή")
        if submitted:
            go_to_end()

# End Page 
elif st.session_state.page == "end":
    st.markdown(
        f"<h1 style='text-align: center; color: {tx_colour}; background-color: #000000; "
        f"padding: 20px; font-family:{font_type};'>STOP AND THINK</h1>",
        unsafe_allow_html=True
    )
    st.image("end_image.png", width=200)

    st.markdown(
        f"<div style='background-color:#000000; padding: 20px; border-radius: 10px;'>"
        f"<p style='color: {tx_colour}; font-family: {font_type}; font-size:16px;'>"
        f"Κοινοποιήσατε ελεύθερα τα προσωπικά σας δεδομένα σε εμάς. "
        f"Απλώς σκεφτείτε τι θα μπορούσε να κάνει ένας εγκληματίας του κυβερνοχώρου με αυτά τα δεδομένα!<br><br>"
        f"<b>Δήλωση αποποίησης ευθύνης:</b> Αυτό το πρόγραμμα στοχεύει να τονίσει τους κινδύνους της ελεύθερης "
        f"υποβολής των προσωπικών σας δεδομένων. Κανένα από τα προσωπικά σας δεδομένα δεν έχει αποθηκευτεί από αυτό το πρόγραμμα."
        f"</p></div>",
        unsafe_allow_html=True
    )

import streamlit as st
import base64

# Assuming your resume is in the same directory as your Streamlit app.
RESUME_PATH = 'Liu_Yichuan_Resume.pdf'

def get_base64_encoded_pdf(pdf_file_path):
    with open(pdf_file_path, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode('utf-8')

# Main app
st.title("Resume Viewer")

# Display PDF in the app
with open(RESUME_PATH, "rb") as pdf_file:
    base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'
st.markdown(pdf_display, unsafe_allow_html=True)

# Download link
with open(RESUME_PATH, 'rb') as pdf_file:
    st.download_button(
        label="Download Resume",
        data=pdf_file,
        file_name="Yichuan_Liu_Resume.pdf",
        mime='application/pdf'
    )

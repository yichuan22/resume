import streamlit as st

# Assuming your resume is in the same directory as your Streamlit app.
RESUME_PATH = 'Liu_Yichuan_Resume.pdf'

# Main app
st.title("Resume Viewer")

# Display link to open PDF in new tab
st.markdown(f'[Open Resume](Liu_Yichuan_Resume.pdf)', unsafe_allow_html=True)

# Download link
with open(RESUME_PATH, 'rb') as pdf_file:
    st.download_button(
        label="Download Resume",
        data=pdf_file,
        file_name="Yichuan_Liu_Resume.pdf",
        mime='application/pdf'
    )


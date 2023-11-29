import streamlit as st
import base64

# Function to encode the PDF for embedding
def get_base64_encoded_pdf(pdf_file_path):
    with open(pdf_file_path, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode('utf-8')

# Main app
def main():
    st.title("Yichuan Liu's Resume")

    # Resume display
    base64_pdf = get_base64_encoded_pdf('Liu_Yichuan_Resume.pdf')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Download link
    with open('Liu_Yichuan_Resume.pdf', 'rb') as pdf_file:
        st.download_button(
            label="Download Resume",
            data=pdf_file,
            file_name="Yichuan_Liu_Resume.pdf",
            mime='application/pdf'
        )

if __name__ == "__main__":
    main()

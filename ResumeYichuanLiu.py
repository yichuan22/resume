import streamlit as st
import os

def main():
    st.title("PDF Viewer")

    # Ensure that the PDF file exists
    pdf_file = 'Liu_Yichuan_Resume.pdf'
    if os.path.exists(pdf_file):
        # Display the PDF
        with open(pdf_file, "rb") as file:
            btn = st.download_button(
                label="Download PDF",
                data=file,
                file_name="example.pdf",
                mime="application/octet-stream"
            )
            st.write("PDF Content:")
            st.components.v1.iframe(src=file.name, width=700, height=1000)
    else:
        st.error("File not found: 'example.pdf'")

if __name__ == "__main__":
    main()

import streamlit as st
from pdf2image import convert_from_path
import os
import tempfile

def main():
    st.title("PDF Viewer")

    pdf_file = 'Liu_Yichuan_Resume.pdf'

    if os.path.exists(pdf_file):
        # Display download button
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name="example.pdf",
                mime="application/octet-stream"
            )

        # Convert PDF to images
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(pdf_file, output_folder=path)

            # Display images
            for page_image in images_from_path:
                st.image(page_image, use_column_width=True)
    else:
        st.error("File not found: 'example.pdf'")

if __name__ == "__main__":
    main()

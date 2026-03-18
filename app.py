import streamlit as st
from PyPDF2 import PdfReader

# Title of the app
st.title('Train Station Extractor')

# File uploader widget
uploaded_file = st.file_uploader('Upload your PDF file', type='pdf')

if uploaded_file is not None:
    # Read the PDF file
    pdf_reader = PdfReader(uploaded_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text() or ''

    # Display the extracted text
    st.subheader('Extracted Data')
    st.write(text)
    
    # Save the extracted data as a text file
    with open('extracted_data.txt', 'w') as f:
        f.write(text)

    st.success('Data extracted and saved as extracted_data.txt')
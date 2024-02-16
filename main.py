import streamlit as st
import pandas as pd

def main():
    st.title("CSV File Viewer")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file)

        # Show the raw data
        st.subheader("Raw Data")
        st.write(df)

        # Show summary statistics
        st.subheader("Summary Statistics")
        st.write(df.describe())

if __name__ == "__main__":
    main()

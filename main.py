import streamlit as st
from pandasai import Agent
import pandas as pd
from pandasai.llm import OpenAI

def main():
    st.title("PandasAI Streamlit App")

    # User Input for API Token
    api_token = st.text_input("Enter your API Token")

    # User Input for CSV File
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    # Load DataFrame if uploaded
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.subheader("Uploaded DataFrame:")
            st.write(df.head())  # Display the first few rows of the DataFrame
        except Exception as e:
            st.error(f"An error occurred while reading the file: {e}")
            return
    else:
        df = None

    # User Input for Query
    query = st.text_input("Enter your query")

    # Perform Query and Display Result
    if api_token and query:
        try:
            # Initialize LLM
            llm = OpenAI(api_token=api_token)

            # Perform query
            if df is not None:
                agent = Agent([df], config={"llm": llm})
                result = agent.chat(query)
                st.subheader("Query Result:")
                st.write(result)
            else:
                st.error("Please upload a CSV file to perform the query.")
        except Exception as e:
            st.error(f"An error occurred while processing the query: {e}")

if __name__ == "__main__":
    main()


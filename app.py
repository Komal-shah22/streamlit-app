import streamlit as st
import pandas as pd
import os
import plotly.express as px
from io import BytesIO

# App Configuration
st.set_page_config(page_title="Advanced Data Processor", layout="wide")

# App Header
st.title("📊 Advanced Data Processor")
st.write("Easily upload, clean, visualize, and convert your CSV/Excel files with advanced features!")

# File Upload Section
uploaded_files = st.file_uploader(
    "Upload your CSV or Excel files", 
    type=["csv", "xlsx"], 
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_ext = os.path.splitext(uploaded_file.name)[-1].lower()

        # Read File
        if file_ext == ".csv":
            df = pd.read_csv(uploaded_file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(uploaded_file)
        else:
            st.error(f"❌ Unsupported file format: {file_ext}")
            continue

        # File Details
        st.subheader(f"📂 File: {uploaded_file.name}")
        st.write(f"**File Size:** {round(uploaded_file.size / 1024, 2)} KB")

        # Data Preview
        st.subheader("🔍 Data Preview")
        st.dataframe(df.head())

        # Data Cleaning Section
        st.subheader("🧹 Data Cleaning Options")
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"Remove Duplicates from {uploaded_file.name}"):
                df.drop_duplicates(inplace=True)
                st.success("✅ Duplicates Removed!")

        with col2:
            if st.button(f"Fill Missing Values in {uploaded_file.name}"):
                numeric_cols = df.select_dtypes(include=["number"]).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.success("✅ Missing Values Filled!")

        # Column Selection & Renaming
        st.subheader("✏️ Select & Rename Columns")
        selected_columns: list[str] = st.multiselect("Choose Columns to Keep", df.columns, default=df.columns)

        if selected_columns:
            df = df[selected_columns]
            rename_dict = {}
            for col in selected_columns:
                new_col_name = st.text_input(f"Rename '{col}' (Leave blank to keep original)", value=col)
                rename_dict[col] = new_col_name
            df.rename(columns=rename_dict, inplace=True)

        # Data Visualization
        st.subheader("📊 Data Visualization")
        chart_type = st.selectbox("Choose Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])

        numeric_columns = df.select_dtypes(include=["number"]).columns
        if not numeric_columns.empty:
            selected_col: str = st.selectbox("Choose Column for Visualization", numeric_columns)

            if chart_type == "Bar Chart":
                fig = px.bar(df, x=df.index, y=selected_col, title=f"Bar Chart of {selected_col}")
            elif chart_type == "Line Chart":
                fig = px.line(df, x=df.index, y=selected_col, title=f"Line Chart of {selected_col}")
            else:
                fig = px.pie(df, names=df.index, values=selected_col, title=f"Pie Chart of {selected_col}")

            st.plotly_chart(fig)

        # File Conversion
        st.subheader("🔄 Convert File")
        conversion_type = st.radio(f"Convert {uploaded_file.name} to:", ["CSV", "Excel"])

        if st.button(f"Convert {uploaded_file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                new_file_name = uploaded_file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:
                df.to_excel(buffer, index=False, engine="xlsxwriter")
                new_file_name = uploaded_file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download Processed File
            st.download_button(
                label=f"⬇️ Download {new_file_name}",
                data=buffer,
                file_name=new_file_name,
                mime=mime_type
            )

            st.success("✅ File Converted & Ready to Download!")


import streamlit as st
import pandas as pd
import os
import plotly.express as px
from io import BytesIO

def main():
    # App Configuration
    st.set_page_config(page_title="Advanced Data Processor", layout="wide")

    # App Header
    st.title("📊 Advanced Data Processor")
    st.write("Upload, clean, visualize, and convert your CSV/Excel files with advanced features!")

    # File Upload Section
    uploaded_files = st.file_uploader("Upload your CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_ext = os.path.splitext(uploaded_file.name)[-1].lower()

            # Read File
            try:
                if file_ext == ".csv":
                    df = pd.read_csv(uploaded_file)
                elif file_ext == ".xlsx":
                    df = pd.read_excel(uploaded_file)
                else:
                    st.error(f"❌ Unsupported file format: {file_ext}")
                    continue
            except Exception as e:
                st.error(f"❌ Error reading file: {e}")
                continue

            # File Details
            st.subheader(f"📂 File: {uploaded_file.name}")
            st.write(f"**File Size:** {round(uploaded_file.size / 1024, 2)} KB")

            # Data Preview
            st.subheader("🔍 Data Preview")
            st.dataframe(df.head())

            # Data Summary
            with st.expander("📜 Data Summary"):
                st.write(df.describe())
                st.write("**Data Types:**")
                st.write(df.dtypes)

            # Data Cleaning Section
            st.subheader("🧹 Data Cleaning Options")
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates ({uploaded_file.name})"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values ({uploaded_file.name})"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("✅ Missing Values Filled!")

            # Advanced Cleaning: Remove Outliers
            if st.checkbox("Remove Outliers (Z-score > 3)"):
                numeric_cols = df.select_dtypes(include=["number"]).columns
                df = df[(df[numeric_cols] - df[numeric_cols].mean()).abs() <= (3 * df[numeric_cols].std())]
                st.success("✅ Outliers Removed!")

            # Custom Filtering
            st.subheader("🔍 Apply Filters")
            filter_column = st.selectbox("Select Column to Filter", df.columns)
            unique_values = df[filter_column].dropna().unique()
            selected_value = st.selectbox("Select Value", unique_values)
            df = df[df[filter_column] == selected_value]

            # Visualization Section
            st.subheader("📈 Learning Analytics Dashboard")

            # Example: Dummy Data for Chart
            sample_data = pd.DataFrame({
                "Day": list(range(1, 31)),
                "Progress Score": [i + (i % 3) * 2 for i in range(1, 31)]
            })

            # Daily Progress Line Chart
            fig_daily = px.line(
                sample_data,
                x="Day",
                y="Progress Score",
                title="Daily Learning Progress",
                labels={"Day": "Day", "Progress Score": "Progress Score"}
            )
            st.plotly_chart(fig_daily)

            # Learning Distribution Pie Chart
            learning_distribution = {
                "Coding Practice": 40,
                "Video Tutorials": 20,
                "Reading Docs": 15,
                "Projects": 25
            }
            fig_pie = px.pie(
                values=list(learning_distribution.values()),
                names=list(learning_distribution.keys()),
                title="Learning Activity Distribution"
            )
            st.plotly_chart(fig_pie)

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
                    df.to_excel(buffer, index=False)
                    new_file_name = uploaded_file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)
                st.download_button(
                    label=f"⬇️ Download {new_file_name}",
                    data=buffer,
                    file_name=new_file_name,
                    mime=mime_type
                )
                st.success("✅ File Converted & Ready to Download!")

# Run App
if __name__ == "__main__":
    main()

# import streamlit as st
# import pandas as pd
# import os
# import plotly.express as px
# from io import BytesIO

# def main():
#     # App Configuration
#     st.set_page_config(page_title="Advanced Data Processor", layout="wide")
    
#     # App Header
#     st.title("📊 Advanced Data Processor")
#     st.write("Upload, clean, visualize, and convert your CSV/Excel files with advanced features!")

#     # File Upload Section
#     uploaded_files = st.file_uploader("Upload your CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             file_ext = os.path.splitext(uploaded_file.name)[-1].lower()
            
#             # Read File
#             if file_ext == ".csv":
#                 df = pd.read_csv(uploaded_file)
#             elif file_ext == ".xlsx":
#                 df = pd.read_excel(uploaded_file)
#             else:
#                 st.error(f"❌ Unsupported file format: {file_ext}")
#                 continue

#             # File Details
#             st.subheader(f"📂 File: {uploaded_file.name}")
#             st.write(f"**File Size:** {round(uploaded_file.size / 1024, 2)} KB")

#             # Data Preview
#             st.subheader("🔍 Data Preview")
#             st.dataframe(df.head())
            
#             # Data Summary
#             with st.expander("📜 Data Summary"):
#                 st.write(df.describe())
#                 st.write("**Data Types:**")
#                 st.write(df.dtypes)

#             # Data Cleaning Section
#             st.subheader("🧹 Data Cleaning Options")
#             col1, col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove Duplicates from {uploaded_file.name}"):
#                     df.drop_duplicates(inplace=True)
#                     st.success("✅ Duplicates Removed!")
            
#             with col2:
#                 if st.button(f"Fill Missing Values in {uploaded_file.name}"):
#                     numeric_cols = df.select_dtypes(include=["number"]).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.success("✅ Missing Values Filled!")

#             # Advanced Cleaning: Remove Outliers
#             if st.checkbox("Remove Outliers (Z-score > 3)"):
#                 numeric_cols = df.select_dtypes(include=["number"]).columns
#                 df = df[(df[numeric_cols] - df[numeric_cols].mean()).abs() <= (3 * df[numeric_cols].std())]
#                 st.success("✅ Outliers Removed!")
            
#             # Custom Filtering
#             st.subheader("🔍 Apply Filters")
#             filter_column = st.selectbox("Select Column to Filter", df.columns)
#             unique_values = df[filter_column].unique()
#             selected_value = st.selectbox("Select Value", unique_values)
#             df = df[df[filter_column] == selected_value]
            
#             # Data Visualization
#             st.subheader("📊 Data Visualization")
#             chart_type = st.selectbox("Choose Chart Type", ["Bar Chart", "Line Chart", "Pie Chart", "Scatter Plot", "Histogram"])
#             numeric_columns = df.select_dtypes(include=["number"]).columns
#             if not numeric_columns.empty:
#                 selected_col = st.selectbox("Choose Column for Visualization", numeric_columns)

#                 if chart_type == "Bar Chart":
#                     fig = px.bar(df, x=df.index, y=selected_col, title=f"Bar Chart of {selected_col}")
#                 elif chart_type == "Line Chart":
#                     fig = px.line(df, x=df.index, y=selected_col, title=f"Line Chart of {selected_col}")
#                 elif chart_type == "Pie Chart":
#                     fig = px.pie(df, names=df.index, values=selected_col, title=f"Pie Chart of {selected_col}")
#                 elif chart_type == "Scatter Plot":
#                     fig = px.scatter(df, x=df.index, y=selected_col, title=f"Scatter Plot of {selected_col}")
#                 else:
#                     fig = px.histogram(df, x=selected_col, title=f"Histogram of {selected_col}")
                
#                 st.plotly_chart(fig)

#             # File Conversion
#             st.subheader("🔄 Convert File")
#             conversion_type = st.radio(f"Convert {uploaded_file.name} to:", ["CSV", "Excel"])
            
#             if st.button(f"Convert {uploaded_file.name}"):
#                 buffer = BytesIO()
#                 if conversion_type == "CSV":
#                     df.to_csv(buffer, index=False)
#                     new_file_name = uploaded_file.name.replace(file_ext, ".csv")
#                     mime_type = "text/csv"
#                 else:
#                     df.to_excel(buffer, index=False, engine="xlsxwriter")
#                     new_file_name = uploaded_file.name.replace(file_ext, ".xlsx")
#                     mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

#                 buffer.seek(0)
#                 st.download_button(
#                     label=f"⬇️ Download {new_file_name}",
#                     data=buffer,
#                     file_name=new_file_name,
#                     mime=mime_type
#                 )
#                 st.success("✅ File Converted & Ready to Download!")

# # Run App
# if __name__ == "__main__":
#     main()







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
            
            # Data Summary
            with st.expander("📜 Data Summary"):
                st.write(df.describe())
                st.write("**Data Types:**")
                st.write(df.dtypes)

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

            # Advanced Cleaning: Remove Outliers
            if st.checkbox("Remove Outliers (Z-score > 3)"):
                numeric_cols = df.select_dtypes(include=["number"]).columns
                df = df[(df[numeric_cols] - df[numeric_cols].mean()).abs() <= (3 * df[numeric_cols].std())]
                st.success("✅ Outliers Removed!")
            
            # Custom Filtering
            st.subheader("🔍 Apply Filters")
            filter_column = st.selectbox("Select Column to Filter", df.columns)
            unique_values = df[filter_column].unique()
            selected_value = st.selectbox("Select Value", unique_values)
            df = df[df[filter_column] == selected_value]
            
            # **Data Visualization**
            st.subheader("📊 Data Visualization")
            if st.checkbox(f"Show Visualization for {uploaded_file.name}"):
                chart_type = st.selectbox("Choose Chart Type", ["Bar Chart", "Line Chart", "Pie Chart", "Scatter Plot", "Histogram"], key=uploaded_file.name)
                numeric_columns = df.select_dtypes(include=["number"]).columns
                if not numeric_columns.empty:
                    x_axis = st.selectbox("Select X-axis", df.columns, key=f"x_{uploaded_file.name}")
                    y_axis = st.selectbox("Select Y-axis", numeric_columns, key=f"y_{uploaded_file.name}")

                    if chart_type == "Bar Chart":
                        fig = px.bar(df, x=x_axis, y=y_axis, title=f"Bar Chart of {y_axis} vs {x_axis}")
                    elif chart_type == "Line Chart":
                        fig = px.line(df, x=x_axis, y=y_axis, title=f"Line Chart of {y_axis} vs {x_axis}")
                    elif chart_type == "Pie Chart":
                        fig = px.pie(df, names=x_axis, values=y_axis, title=f"Pie Chart of {y_axis}")
                    elif chart_type == "Scatter Plot":
                        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter Plot of {y_axis} vs {x_axis}")
                    else:
                        fig = px.histogram(df, x=y_axis, title=f"Histogram of {y_axis}")
                    
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


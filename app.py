import os
import pandas as pd
import streamlit as st


#import profiling
import streamlit_pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport


#import for ml model
from pycaret.classification import setup,pull,save_model,compare_models 





imgUrl="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1530&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

with st.sidebar:
    st.title("Auto ML")
    st.image(imgUrl, width=150)
    choice=st.radio("Navigation", ["Upload Data", "Profiling", "Ml", "Download Model"])
    st.info("This application is created by [  SAISRISATYA ](https://www.linkedin.com/in/padala-sai-sri-satya-subramaneswar-359998247/)")

if os.path.exists("UploadedData.csv"):
    df=pd.read_csv("UploadedData.csv",index_col=None)
    # st.dataframe(df)
    # st.write("Data is uploaded")


if choice =="Upload Data":
    st.title("Upload Data for the Modeling")
    st.write("upload only CSV files.")
    file = st.file_uploader("Upload file", type=["csv"])
    if file:
        df=pd.read_csv(file,index_col=None)
        df.to_csv("UploadedData.csv",index=False)
        st.dataframe(df)
    


    
        
# if choice =="Profiling":
#     st.write("Automated EDAs")
#     st.write("Profiling")
#     profile_report=ProfileReport(df, title="Pandas Profiling Report", explorative=True)
#     st_profile_report(profile_report)
if choice == "Profiling":
    st.write("Automated EDAs")
    st.write("Profiling")

    # Display loading spinner
    with st.spinner("Profiling in progress..."):
        # Generate Pandas Profiling report
        profile_report = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

    # Render the HTML report
    st_profile_report(profile_report)

    # Display completion message
    st.success("Profiling completed.")


# if choice == "Ml":
#     st.title("Machine Learning Model") 
#     st.write("Please select the target variable - means which column you want to predict")   
#     target = st.selectbox("Select Target Variable", df.columns)
#     setup(data=df, target=target)
    # setup_df = pull()
    # st.info("This is the setup data")
    # st.dataframe(setup_df)
    # best_model = compare_models()
    # compare_df=pull()
    # st.info("This is the ML model")
    # st.dataframe(compare_df)
    # st.write(compare_df)

    # best_model
if choice == "Ml":
    st.title("Machine Learning Model") 
    st.write("Please select the target variable - means which column you want to predict")   
    target = st.selectbox("Select Target Variable", df.columns)
    if st.button("Run ML Model"):
        


        # Check and handle class imbalance here if needed
        # class_counts = df[target].value_counts()
        # rare_classes = class_counts[class_counts == 1].index.tolist()

        # # Remove rare classes or aggregate them
        # df[target] = df[target].apply(lambda x: "Other" if x in rare_classes else x)
        # df[target] = pd.to_numeric(df[target], errors='coerce')

        # st.write( df[target])
        # st.write( df.dtypes)

        # setup(data=df, target=target,verbose = False,fix_imbalance=True)
        try:
            setup(data=df, target=target,verbose = False,fix_imbalance=True)

            setup_df = pull()

            if not setup_df.empty:
                st.info("This is the setup data")
                st.dataframe(setup_df)

            # Handle class imbalance if needed after setup
            # oversample or undersample or use other techniques
            else:
                st.warning("No data available in the setup. Please select the different column.")

        except Exception as e:
            st.warning("No data available in the setup. Please select the different column.")



        with st.spinner("Please wait your model is building..."):
            best_model = compare_models()
            compare_df = pull()
            st.info("This is the ML model")
            st.dataframe(compare_df) 

            best_model
            save_model(best_model, 'best_model')
            st.success("Model is built successfully. Please download the best model for further use.")

    

if choice == "Download Model":
    st.write("Download Model")
    with open("best_model.pkl", "rb") as f:
        st.download_button("Download Model", f, file_name="best_trained_model.pkl ")

 
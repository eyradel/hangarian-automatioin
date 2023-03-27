import streamlit as st
import numpy as np
from scipy.optimize import linear_sum_assignment
import pandas as pd
import time
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            <html><body><p></p><body/></html>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def hungarian_algorithm(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_ind, col_ind].sum()
    return row_ind, col_ind, total_cost,

st.title("The Hungarian Algorithm")
st.subheader(" for to solving Assignment Problem")
st.text("CE4") 
st.markdown("https://delaeyram.com")
col1,col2 = st.columns(2)
# Get the size of the matrix from the user
with col1:
    matrix_size = st.number_input("Enter the size of the matrix", min_value=1, max_value=10, value=3)

# Create an empty matrix
    matrix = np.zeros((matrix_size, matrix_size))
    
    # Fill in the matrix with user input

    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix[i][j] = st.number_input(f"Enter the cost for row {i+1}, column {j+1}", min_value=0)

# Run the algorithm when the user clicks the button
with col2:
    
        
    if st.button("Run"):
        with st.spinner("Performing Calculations......"):
            
            time.sleep(3)
            row_ind, col_ind, total_cost = hungarian_algorithm(matrix)
            st.write("Optimal assignment:")
            for i in range(matrix_size):
                
                #st.write(f"Worker {row_ind[i]+1} is assigned to Job {col_ind[i]+1}")
                df = pd.DataFrame({ "Worker":[row_ind[i]+1],"Cost": [int(matrix[row_ind[i]][col_ind[i]])], "Job": [col_ind[i]+1],})
                st.table(df)
                st.write(f"Worker {row_ind[i]+1} is assigned to Job {col_ind[i]+1} (Cost: {int(matrix[row_ind[i]][col_ind[i]])})")
            st.metric(f"Total cost: ",total_cost)
    
    
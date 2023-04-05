import streamlit as st
import numpy as np
from scipy.optimize import linear_sum_assignment
import pandas as pd
import time
import plotly.graph_objects as go

session_state = st.session_state
session_state.cache = False
#st.markdown('<h2 class="text-primary">Hungarian Algorithm</h2>', unsafe_allow_html=True)
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">', unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
     
            header{visibility:hidden;}
            
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            
            """
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: orange;">
  <a class="navbar-brand" href="#"  target="_blank">Assignment Problem solver</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
   
  </button>
  
</nav>
""", unsafe_allow_html=True)

    
    # Display some example content with the MDB Bootstrap style

#st.markdown('<p class="text-secondary">This is some secondary text</p>', unsafe_allow_html=True)

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def hungarian_algorithm(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_ind, col_ind].sum()
    return row_ind, col_ind, total_cost,

#st.title("The Hungarian Algorithm")
#st.subheader(" for to solving Assignment Problem")
#st.text("CE4") 

col1,col2 = st.columns(2)
# Get the size of the matrix from the user
with col1:
    matrix_size = st.number_input("Enter the size of the matrix", min_value=1, max_value=10, value=1)

# Create an empty matrix
    matrix = np.zeros((matrix_size, matrix_size))
    
    # Fill in the matrix with user input

    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix[i][j] = st.number_input(f"Enter the cost for row {i+1}, column {j+1}", min_value=0)

# Run the algorithm when the user clicks the button
with col2:
    
        
    if st.button("Run",):
        with st.spinner("Performing Calculations......"):
            
            time.sleep(3)
            row_ind, col_ind, total_cost = hungarian_algorithm(matrix)
            st.write("Optimal assignment:")
            for i in range(matrix_size):
                
                #st.write(f"Worker {row_ind[i]+1} is assigned to Job {col_ind[i]+1}")
                df = pd.DataFrame({ "Worker":[row_ind[i]+1],"Cost": [int(matrix[row_ind[i]][col_ind[i]])], "Job": [col_ind[i]+1],})
                st.table(df)
                st.write(f"Worker {row_ind[i]+1} is assigned to Job {col_ind[i]+1} (Cost: {int(matrix[row_ind[i]][col_ind[i]])})")
            st.markdown('<p class="text-secondary">Optimal Cost :</p>', unsafe_allow_html=True)
            st.metric(f"",total_cost)
            data = []
            labels = [f"Worker {i+1}" for i in range(matrix_size)] + [f"Job {j+1}" for j in range(matrix_size)]
            for i in range(matrix_size):
                for j in range(matrix_size):
                    data.append([i, matrix_size+j, matrix[i][j]])
            fig = go.Figure(data=[go.Sankey(
                node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=labels,
                color="blue"
                ),
                link=dict(
                source=[data[i][0] for i in range(len(data))],
                target=[data[i][1] for i in range(len(data))],
                value=[data[i][2] for i in range(len(data))],
                ))])
            fig.update_layout(title_text="Visualization")
            st.plotly_chart(fig)

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)    

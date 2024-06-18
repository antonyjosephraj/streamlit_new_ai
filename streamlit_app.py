# import streamlit as st

# # First section in the sidebar
# st.sidebar.title('Section 1')
# option1 = st.sidebar.selectbox('Choose an option', ['Option A', 'Option B', 'Option C'])

# # Second section in the sidebar
# st.sidebar.title('Section 2')
# option2 = st.sidebar.slider('Choose a value', 0, 100, 50)

# # Third section in the sidebar
# st.sidebar.title('Section 3')
# option3 = st.sidebar.checkbox('Show details')

# # Main content of the app
# st.title('Main Content')

# # Display selected options from the sidebar
# st.write('Option selected in Section 1:', option1)
# st.write('Value selected in Section 2:', option2)
# st.write('Checkbox state in Section 3:', option3)


# import streamlit as st

# # Define function for each "page" or section
# def page_section1():
#     st.title('Section 1')
#     option1 = st.selectbox('Choose an option', ['Option A', 'Option B', 'Option C'])
#     st.write('Option selected:', option1)

# def page_section2():
#     st.title('Section 2')
#     option2 = st.slider('Choose a value', 0, 100, 50)
#     st.write('Value selected:', option2)

# def page_section3():
#     st.title('Section 3')
#     option3 = st.checkbox('Show details')
#     st.write('Checkbox state:', option3)

# # Create sidebar navigation
# navigation = st.sidebar.radio('Navigation', ['Section 1', 'Section 2', 'Section 3'])

# # Render the selected "page" based on navigation choice
# if navigation == 'Section 1':
#     page_section1()
# elif navigation == 'Section 2':
#     page_section2()
# elif navigation == 'Section 3':
#     page_section3()



# import streamlit as st

# # Define function for each "page" or section
# def page_section1():
#     st.title('Section 1')
#     option1 = st.selectbox('Choose an option', ['Option A', 'Option B', 'Option C'])
#     st.write('Option selected:', option1)

# def page_section2():
#     st.title('Section 2')
#     option2 = st.slider('Choose a value', 0, 100, 50)
#     st.write('Value selected:', option2)

# def page_section3():
#     st.title('Section 3')
#     option3 = st.checkbox('Show details')
#     st.write('Checkbox state:', option3)

# # Create sidebar with menu items
# menu_selection = st.sidebar.selectbox('Menu', ['Section 1', 'Section 2', 'Section 3'])

# # Render the selected "page" based on menu selection
# if menu_selection == 'Section 1':
#     page_section1()
# elif menu_selection == 'Section 2':
#     page_section2()
# elif menu_selection == 'Section 3':
#     page_section3()



# import streamlit as st

# # Define the sidebar menu options as Markdown links
# st.sidebar.title('Menu')
# if st.sidebar.markdown("[Home](#)", unsafe_allow_html=True):
#     st.title('Home Page')
#     st.write('Welcome to the Home page.')
# elif st.sidebar.markdown("[About](#)", unsafe_allow_html=True):
#     st.title('About Page')
#     st.write('This is the About page.')
# elif st.sidebar.markdown("[Contact](#)", unsafe_allow_html=True):
#     st.title('Contact Page')
#     st.write('Contact us at contact@example.com')


# import streamlit as st

# # Define the sidebar menu options as Markdown links
# st.sidebar.title('Menu')

# # Define the selected page variable
# selected_page = None

# # Render the sidebar menu options as Markdown links
# if st.sidebar.markdown("[Home](#)"):
#     selected_page = 'Home'
# elif st.sidebar.markdown("[About](#)"):
#     selected_page = 'About'
# elif st.sidebar.markdown("[Contact](#)"):
#     selected_page = 'Contact'

# # Function to display content based on selection
# def display_content(selected_page):
#     if selected_page == 'Home':
#         st.title('Home Page')
#         st.write('Welcome to the Home page.')
#     elif selected_page == 'About':
#         st.title('About Page')
#         st.write('This is the About page.')
#     elif selected_page == 'Contact':
#         st.title('Contact Page')
#         st.write('Contact us at contact@example.com')

# # Display content based on the selected page
# if selected_page:
#     display_content(selected_page)



import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

# # Define sidebar menu options
# menu_options = {
#     "Pickups": pickups,
#     "Drops": drops,
# }
st.title('POC')      
st.text('Identify the specifics of data input and delineate the operational functionalities.')

st.image('ai.jpg')


st.title("CHART'S")      
data=pd.read_csv('data_inputs.csv')    
df= pd.DataFrame(   data,    columns=['Invested Amount', 'Multiple at Exit'])
st.line_chart(df)

st.markdown('Dataset :')   
data=pd.read_csv('sample_data.csv')    
st.write(data.head()) 
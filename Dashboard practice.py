import streamlit as st

# Title and Header
st.title("Retail Business Dashboard")
st.header("Manager input section")

# Instruction
st.write("please enter the monthly sales target and select the region")

# Number input for sales target
target = st.number_input("Enter Monthly Sales Target(in USD):",
                      min_value=0,
                      max_value=50000,
                      value=0)

# Dropdown for region selection
region = st.selectbox("Select Region:",
                      ["North", "South", "East", "West"])

# Submit button
if st.button("Submit"):
    # Display entered values
  st.write(f"the monthly sales target: {target}")
  st.write(f"the region: {region}")
  

    # Success message
st.success("Operation completed successfully!")


    # Extra message for ambitious target

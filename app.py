import streamlit as st
import re

# Function to generate a random color
def generate_color(first_name, middle_name, last_name):
    # first_name:R , middle_name:G, last_name:B
    def calculate_name_value(name):
        # Remove special characters and make lowercase
        cleaned_name = re.sub(r'[^a-z]', '', name.lower())
        # Calculate the sum of letters where 'a' = 0, ..., 'z' = 25
        return sum(ord(char) - ord('a') for char in cleaned_name)

    # Step 1: Calculate nr, ng, nb
    nr = calculate_name_value(first_name)
    ng = calculate_name_value(middle_name)
    nb = calculate_name_value(last_name)

    nr *= 4
    ng *= 4
    nb *= 4

    vr = nr % 256
    vg = ng % 256
    vb = nb % 256

    hex_color = "#{:02x}{:02x}{:02x}".format(vr, vg, vb)
    return hex_color

st.set_page_config(page_title="Name-o-Color",
                    page_icon="🖌️",
                    layout="wide")

st.markdown("# Get the Color of your Name")

st.write("Type your name to see the unique color corresponding to it.")

# Centering the content
st.markdown(
    """
    <style>
    div.block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    div.row {
        display: flex;
        justify-content: space-between;
        width: 60%;
    }
    div.stButton {
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Layout for the input fields
st.markdown('<div class="row">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    first_name = st.text_input("First Name", max_chars=50)
with col2:
    middle_name = st.text_input("Middle Name", max_chars=50)
with col3:
    last_name = st.text_input("Last Name", max_chars=50)
st.markdown('</div>', unsafe_allow_html=True)

# Button to generate color
if st.button("Generate Color"):
    color = generate_color(first_name, middle_name, last_name)
    # Display color and hex code
    st.write(f"Generated Color: **{color}**")
    st.markdown(
        f"""
        <div style="width: 100px; height: 50px; background-color: {color}; margin-top: 10px; border: 1px solid #000;"></div>
        """,
        unsafe_allow_html=True,
    )

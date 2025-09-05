import streamlit as st
from few_shot import few_short
from post_generater import generate_post


length_options = ["short", "medium", "long"]
language_options = ["English", "Hinglish"]

def main():
    st.subheader("linkedin post generator")
    col1,col2,col3 = st.columns(3)
    fs = few_short()
    tags = fs.get_tags()
    with col1:
        selected_tag =  st.selectbox("topic",options=tags)
    with col2:
        selected_length = st.selectbox("Length", options=length_options) 
    with col3:
        selected_language = st.selectbox("Language", options=language_options)
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)
# Run the app
if __name__ == "__main__":
    main()
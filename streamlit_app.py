from Workflows.graph import run_pipeline
import streamlit as st
import asyncio


st.set_page_config(
    page_title="Linked In Content Generator",
     page_icon="🚀",
    layout="wide"
)

st.title("LinkedIn Content Generator")

repo_url = st.text_input(
    "Github repostory URL",
    placeholder="https://github.com/owner/repo"
)
audiences = st.multiselect(
    "Target Audiences",
     ["developers", "non-developers", "LinkedIn"],
     default=['developers','non-developers']
)
if st.button("Generate Content"):

    if not repo_url:
        st.error("Pleae enter a repository URL")
    else:
        st.spinner("Analyzing repository...")
    
        result = asyncio.run(
            run_pipeline(
                repo_url,audiences
            )
        )
    st.success("Done!")

    st.subheader("Plan")
    st.write(result['plan'])

    # st.subheader("Research")
    # st.json(result['research'])

    st.subheader("Draft")
    st.markdown(result['draft'])

    st.subheader("Review")
    st.markdown(result['review'])
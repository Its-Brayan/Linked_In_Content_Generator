from Workflows.graph import run_pipeline
import streamlit as st
import asyncio
import subprocess
import os
from groq import RateLimitError
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
     try:
        st.spinner("Analyzing repository...")
    
        result = asyncio.run(
            run_pipeline(
                repo_url,audiences
            )
        )
     except RateLimitError as e:
        st.error("🚨 **Rate Limit Exceeded:** The AI provider is currently out of tokens. Please try again in a few minutes.")
        with st.expander("View detailed error"):
                st.write(e)
     except Exception as e:
            # Catch-all for any other workflow errors (e.g., bad Github URL, tool failure)
            st.error("An unexpected error occurred during generation.")
            st.exception(e)
    st.success("Done!")

    st.subheader("Plan")
    st.write(result['plan'])

    # st.subheader("Research")
    # st.json(result['research'])

    st.subheader("Draft")
    st.markdown(result['draft'])

    st.subheader("Review")
    st.markdown(result['review'])

@st.cache_resource
def start_mcp_server():
    env = os.environ.copy()
    env['npm_config_cache'] ="/tmp/.npm"
    process = subprocess.Popen(
        ["npx", "-y", "@modelcontextprotocol/server-github"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env
    )
    return process

# Initialize your server
mcp_process = start_mcp_server()

st.success("MCP Server is running in the background!")
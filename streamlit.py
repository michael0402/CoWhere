import streamlit as st
from retrieve import Chatbot, Documents  # import your Chatbot and Documents classes

# Define your sources
sources = [
    {
        "title": "Find Manpages",
        "url": "https://ss64.com/osx/find.html"},
    {
        "title": "setup.sh",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/setup.sh"},
    {
        "title": "README.md",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/README.md"},
    {
        "title": "CMakeLists.txt",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/CMakeLists.txt"},
    {
        "title": ".gitignore",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/.gitignore"},
    {
        "title": ".chris_zsh",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/.chris_zsh"},

    {
        "title": ".chris_bash",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/.chris_bash"},
    {
        "title": "main.cpp",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/src/main.cpp"},
    {
        "title": "gpt.hpp",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/src/gpt.hpp"},
    {
        "title": "gpt.cpp",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/src/gpt.cpp"},
    {
        "title": "context.hpp",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/src/context.hpp"},
    {
        "title": "cmake-multi-platform.yml",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/.github/workflows/cmake-multi-platform.yml"},
    {
        "title": "c-cpp.yml",
        "url": "https://raw.githubusercontent.com/CommanderChrisOrg/CommanderChris/main/.github/workflows/c-cpp.yml"}
]

# Initialize the Documents and Chatbot
documents = Documents(sources)
chatbot = Chatbot(documents)

# Streamlit interface
def main():
    st.title("RAG-Powered Chatbot")
    
    user_input = st.text_input("Your message", key="user_input")

    if st.button("Send"):
        progress_bar = st.progress(0)
        with st.spinner('Generating response...'):
            response = chatbot.generate_response(user_input)
            response_text = ""
            citations = []

            # Assuming a maximum of 100 steps for the progress bar
            step = 0
            max_steps = response_text.__sizeof__()

            for event in response:
                if event.event_type == "text-generation":
                    response_text += event.text
                if event.event_type == "citation-generation":
                    citations.append(event.citations)
                
                # Update the progress bar
                step += 1
                progress = min(step / max_steps, 1.0)  # Ensure progress does not exceed 1.0
                progress_bar.progress(progress)

        st.write(response_text)
        for citation in citations:
            st.write("Citation:", citation)
        st.balloons()

if __name__ == "__main__":
    main()
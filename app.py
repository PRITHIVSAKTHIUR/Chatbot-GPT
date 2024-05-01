import streamlit as st
from huggingface_hub import InferenceClient
import os
import sys

st.title("strangerzone.world🗞️")

base_url="https://api-inference.huggingface.co/models/"

API_KEY = os.environ.get('HUGGINGFACE_API_KEY')
# print(API_KEY)
# headers = {"Authorization":"Bearer "+API_KEY}

model_links ={
    "Dorado🥤":base_url+"mistralai/Mistral-7B-Instruct-v0.2",
    "Hercules⭐":base_url+"mistralai/Mixtral-8x7B-Instruct-v0.1",
    "Lepus🚀":base_url+"microsoft/Phi-3-mini-4k-instruct"
}



#Pull info about the model to display
model_info ={
    "Dorado🥤":
        {'description':"""The Dorado model is a **Large Language Model (LLM)** that's able to have question and answer interactions.\n \
            \nThis model is best for minimal problem-solving, content writing, and daily tips.\n""",
        'logo':'./dorado.png'},

    
    "Hercules⭐":
        {'description':"""The Hercules model is a **Large Language Model (LLM)** that's able to have question and answer interactions.\n \
            \nThis model excels in coding, logical reasoning, and high-speed inference. \n""",
        'logo':'./hercules.png'},

    
      "Lepus🚀":        
      {'description':"""The Lepus model is a **Large Language Model (LLM)** that's able to have question and answer interactions.\n \
          \nThis model is best suited for critical development, practical knowledge, and serverless inference.\n""",
      'logo':'./lepus.png'},

    
}

def format_promt(message, custom_instructions=None):
    prompt = ""
    if custom_instructions:
        prompt += f"[INST] {custom_instructions} [/INST]"
    prompt += f"[INST] {message} [/INST]"
    return prompt

def reset_conversation():
    '''
    Resets Conversation
    '''
    st.session_state.conversation = []
    st.session_state.messages = []
    return None

models =[key for key in model_links.keys()]

# Create the sidebar with the dropdown for model selection
selected_model = st.sidebar.selectbox("Select Model", models)

#Create a temperature slider
temp_values = st.sidebar.slider('Select a temperature value', 0.0, 1.0, (0.5))

#Add reset button to clear conversation
st.sidebar.button('Reset Chat', on_click=reset_conversation) #Reset button

# Create model description
st.sidebar.write(f"You're now chatting with **{selected_model}**")
st.sidebar.markdown(model_info[selected_model]['description'])
st.sidebar.image(model_info[selected_model]['logo'])
st.sidebar.markdown("*Generated content may be inaccurate or false.*")
st.sidebar.markdown("\nYou can support me by sponsoring to buy me a coffee🥤.[here](https://buymeacoffee.com/prithivsakthi).")

if "prev_option" not in st.session_state:
    st.session_state.prev_option = selected_model

if st.session_state.prev_option != selected_model:
    st.session_state.messages = []
    # st.write(f"Changed to {selected_model}")
    st.session_state.prev_option = selected_model
    reset_conversation()

#Pull in the model we want to use
repo_id = model_links[selected_model]

st.subheader(f'{selected_model}')
# st.title(f'ChatBot Using {selected_model}')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
if prompt := st.chat_input(f"Hi I'm {selected_model}🗞️, How can I help you today?"):

    custom_instruction = "Act like a Human in conversation"

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    formated_text = format_promt(prompt, custom_instruction)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        client = InferenceClient(
            model=model_links[selected_model],)
            # headers=headers)

        output = client.text_generation(
            formated_text,
            temperature=temp_values,#0.5
            max_new_tokens=3000,
            stream=True
        )

        response = st.write_stream(output)
    st.session_state.messages.append({"role": "assistant", "content": response})

from tempfile import NamedTemporaryFile
import streamlit as st
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

from tools import ImageCaptionTool, ObjectDetectionTool

## Initializing Agent
tools = [ImageCaptionTool(), ObjectDetectionTool()]

conversational_memory = ConversationBufferWindowMemory(
   memory_key='chat_history',
   k=5,
   return_messages=True
)

llm = ChatOpenAI(
   openai_api_key='YOUR_API_KEY',
   temperature=0,
   model_name="gpt-3.5-turbo"
)

agent = initialize_agent(
   agent="chat-conversational-react-description",
   tools=tools,
   llm=llm,
   max_iterations=5,
   verbose=True,
   memory=conversational_memory,
   early_stopping_method='generate'
)


# Set Title
st.title('Ask The Image')

# Set Header
st.header('Upload an image and ask it some questions about it')

# Uploading The File

file = st.file_uploader("", type=["jpeg", "jpg", "png"])

if file:
   # Display Image
   st.image(file, use_column_width=True)

   # Text Input
   user_question = st.text_input('Ask a question about your image:')
   
   # Generate Agent Response
   with NamedTemporaryFile(dir='.') as f:
      f.write(file.getbuffer())
      image_path = f.name

      # Write agent response
      if user_question and user_question != "":
         with st.spinner(text="In progress..."):
               response = agent.run('{}, this is the image path: {}'.format(user_question, image_path))
               st.write(response)

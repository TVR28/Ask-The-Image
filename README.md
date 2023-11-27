# Ask The Image

This is a Streamlit application that allows users to ask questions about an uploaded image and receive responses from a conversational AI agent. The agent leverages the OpenAI GPT-3.5 Turbo model to generate answers based on the provided image and user questions.

<p align="center">
<a>
    <img width="1000" src="output.JPG">
</a>
</p>

## installation

1. Clone the repository:

        git clone https://github.com/your-username/image-question-answering.git
        
2. Change to the project directory:

        cd  ask-question-image-web-app-streamlit-langchain
        
3. Install the required dependencies:

        pip install -r requirements.txt

4. Obtain an **OpenAI API key**. You can sign up for an API key at [OpenAI](https://platform.openai.com).

5. Replace the placeholder API key in the main.py file with your actual OpenAI API key:

        llm = ChatOpenAI(
            openai_api_key='YOUR_API_KEY',
            temperature=0,
            model_name="gpt-3.5-turbo"
        )

6. Run the Streamlit application:

        streamlit run main.py

7. Open your web browser and go to http://localhost:8501 to access the application.

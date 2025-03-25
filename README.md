# Simple-AI-Agent
A simple AI chatbot agent built using Streamlit, Groq API, and DuckDuckGo Search. The chatbot can respond to user queries using an AI model and fetch web search results.
![image](https://github.com/user-attachments/assets/c1987bd8-898b-4e9a-b557-d19d0edc4a1e)
# Features
- AI-powered chatbot using Groq LLM
- Web search capability using DuckDuckGo
- Interactive Streamlit UI
- Custom styling for enhanced user experience
![image](https://github.com/user-attachments/assets/6d8322a2-4a40-4f1c-b7de-9eacd4e5fc7a)
# Installation
- Python 3.8+
- A Groq API Key
- Virtual environment (optional but recommended)

# Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/simple-ai-agent.git
   cd simple-ai-agent
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Create a .env file in the project root and add your Groq API key:
    ```bash
    GROQ_API_KEY=your_api_key_here

# Usage
- Run the streamlit app:
  ```bash
  streamlit run app.py
# File Structure
- ```bash
  ├── app.py            # Main application script
  ├── requirements.txt  # List of dependencies
  ├── .env.example      # Example environment variables file
  ├── README.md         # Project documentation
  ├── .gitignore        # Ignoring unnecessary files
  └── LICENSE           # Project license file

# License
This project is licensed under the MIT License.

# Contributing
Feel free to open issues or submit pull requests for improvements!

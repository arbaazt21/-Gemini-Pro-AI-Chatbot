# 🤖 Gemini-Pro AI Chatbot

Gemini-Pro AI Chatbot is an intelligent conversational AI powered by Google GeminiPro, integrated into a user-friendly Streamlit interface. This project enables seamless interactions with the Gemini-Pro model for generating dynamic and insightful responses to user queries.

Ask anything to my CHATBOT -->>> [Click](https://huggingface.co/spaces/arbaazt21/Gemini-Pro-AI-Chatbot)


## 📋 Features
- **Powered by Google GeminiPro AI**: Leverage advanced natural language processing capabilities.
- **Streamlit Interface**: A clean and interactive UI for users.
- **Session History**: Maintains conversation context for dynamic, contextual responses.
- **Environment Variable Configuration**: Secures your API key using `.env`.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gemini-pro-chatbot.git
   cd gemini-pro-chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

---

## 🚀 Usage

1. Run the chatbot application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

3. Start interacting with the Gemini-Pro AI Chatbot!

---

## 🗂️ Project Structure
```plaintext
📁 gemini-pro-chatbot/
├── 📄 app.py                # Main Streamlit app script
├── 📄 .env                  # Environment variables (not included in the repo)
├── 📄 requirements.txt      # Python dependencies
└── 📄 README.md             # Project documentation
```

---

## 🌟 How It Works

1. **Environment Configuration**: The API key for Google GeminiPro is securely loaded from a `.env` file.
2. **Streamlit Integration**: Streamlit provides an interactive and dynamic user interface.
3. **GeminiPro Model**: Chatbot functionality is powered by the Gemini-Pro model from Google Generative AI.
4. **Session Management**: Conversations are persisted for continuity using `st.session_state`.

---

## 📌 Prerequisites
- Python 3.7 or above
- Google GeminiPro API access (requires a valid API key)

---

## 🚀 Deployment
The web application for this project is deployed on [HuggingFace](https://gemini-pro-ai-chatbot.onrender.com)  , providing an accessible interface for users to interact with the Chatbot and get real-time Experience.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

---

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## ✉️ Contact
For questions or feedback, reach out via [arbaazt2002@gmail.com].

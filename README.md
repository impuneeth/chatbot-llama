# **Chatbot with Llama 3.2**

This project is a **conversational AI chatbot** built using **Streamlit** as the frontend framework and **Together AI's Llama 3.2** as the language model backend. The chatbot provides an interactive and user-friendly interface for answering questions and analyzing user-provided content.

## **Features**
- **Simple Chat Interface**: Engage with the chatbot to ask questions and get AI-powered responses.
- **Document Analysis**: Upload a document and interact with its content using the chatbot.
- **Real-time Conversations**: Powered by Llama 3.2, offering accurate and context-aware responses.
- **Streamlit Integration**: A clean, minimalistic, and responsive UI built with Streamlit.

## **Technologies Used**
1. **Frontend**:  
   - [Streamlit](https://streamlit.io/) for creating the interactive UI.  

2. **Backend**:  
   - [Together AI](https://together.ai/) for serving the **Llama 3.2** Large Language Model (LLM).  

3. **Languages**:  
   - Python for the application logic.

---

## **Installation and Setup**
### **1. Prerequisites**
Ensure you have the following installed:  
- Python 3.8+  
- pip (Python package installer)  

### **2. Clone the Repository**
```bash
git clone <repository-url>
cd <repository-folder>
```

### **3. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **4. Set Up Together AI API**
- Obtain your API key from [Together AI](https://together.ai/).  
- Add the API key to your project as an environment variable or directly in the code:
  ```bash
  export TOGETHERAI_API_KEY=your_api_key
  ```

### **5. Run the Application**
Start the Streamlit server:
```bash
streamlit run app.py
```

### **6. Access the Chatbot**
Open your browser and navigate to:
```
http://localhost:5004
```

## **Usage**
1. **Chat Interface**:
   - Start a conversation by typing a question or statement into the input box.
   - Get intelligent responses from the Llama 3.2 LLM.

2. **Document Chat**:
   - Upload a document to analyze its content interactively.
   - Ask specific questions about the uploaded document.

## **Acknowledgments**
- **Streamlit** for making UI development simple and intuitive.  
- **Together AI** for providing access to Llama 3.2, enabling robust conversational AI.  
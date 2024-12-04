# Chatbot-AI-For_MY_UNIVERSITY

USTC AI Chatbot
An Intelligent Chatbot for University Students
# Project Description
The USTC AI Chatbot is an advanced multilingual conversational assistant designed to help students and prospective applicants with questions about university admissions, departmental information, tuition fees, and more.

# Key Features:

1,Multilingual Support: Handles English, Bangla, and Banglish queries.<br>
2.Quick Responses: Processes and responds to queries in real-time.<br>
3.User-Friendly Interface: Built with Gradio, offering an intuitive and visually appealing chat experience.<br>
4.Core NLP Components: Integrates language processing and embedding generation for accurate answers.<br>
# Screenshots
![image](https://github.com/user-attachments/assets/337db4c4-856c-42e4-9cf6-7f8784923adb)

# Technologies Used
1.Python: Backend development.<br>
2.Gradio: Chatbot UI framework.<br>
3.LangChain: For NLP and RAG pipeline implementation.<br>
4.Pinecone: Vector database for document storage and retrieval.<br>
4.NVIDIA AI Endpoints: Pre-trained models for embedding and response generation.<br>
5.Setup Instructions<br>
6.Requirements <br>
7.Python 3.8 or above <br>
8.API keys for NVIDIA AI and Pinecone (stored in .env file) <br>
9.Installation <br>

# How it Works
1. User Query: The user inputs a question in English, Bangla, or Banglish.<br>
2. Processing: The chatbot uses LangChain to retrieve relevant information from the knowledge base (e.g., Pinecone).<br>
3. Response: The chatbot generates a quick and accurate response using NVIDIA AI models.<br>
4. Interface: The response is displayed in the Gradio chat interface.<br>

# Future Enhancements
1.Add voice input/output support.<br>
2.Expand the database for broader query coverage.<br>
3.Integrate with real-time university updates.<br>

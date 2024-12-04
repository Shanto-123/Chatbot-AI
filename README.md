# Chatbot-AI-For_MY_UNIVERSITY

USTC AI Chatbot
An Intelligent Chatbot for University Students
Project Description
The USTC AI Chatbot is an advanced multilingual conversational assistant designed to help students and prospective applicants with questions about university admissions, departmental information, tuition fees, and more.

# Key Features:

Multilingual Support: Handles English, Bangla, and Banglish queries.
Quick Responses: Processes and responds to queries in real-time.
User-Friendly Interface: Built with Gradio, offering an intuitive and visually appealing chat experience.
Core NLP Components: Integrates language processing and embedding generation for accurate answers.
# Screenshots
![image](https://github.com/user-attachments/assets/337db4c4-856c-42e4-9cf6-7f8784923adb)

# Technologies Used
1.Python: Backend development.
2.Gradio: Chatbot UI framework.
3.LangChain: For NLP and RAG pipeline implementation.
4.Pinecone: Vector database for document storage and retrieval.
4.NVIDIA AI Endpoints: Pre-trained models for embedding and response generation.
5.Setup Instructions
6.Requirements
7.Python 3.8 or above
8.API keys for NVIDIA AI and Pinecone (stored in .env file)
9.Installation

# How it Works
User Query: The user inputs a question in English, Bangla, or Banglish.
Processing: The chatbot uses LangChain to retrieve relevant information from the knowledge base (e.g., Pinecone).
Response: The chatbot generates a quick and accurate response using NVIDIA AI models.
Interface: The response is displayed in the Gradio chat interface.

# Future Enhancements
Add voice input/output support.
Expand the database for broader query coverage.
Integrate with real-time university updates.

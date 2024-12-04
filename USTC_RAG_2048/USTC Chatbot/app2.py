import gradio as gr
from gradio import ChatMessage
from utils.assistant import UniversityAssistant
from dotenv import load_dotenv

# Load environment variables and initialize the assistant
load_dotenv()
assistant = UniversityAssistant(index_name="ustc-rag-2048")

# Function to handle user input and bot responses
def chat_with_bot(history, user_message):
    if user_message.strip():
        # Append user message to history
        history.append(ChatMessage(role="user", content=user_message))
        # Generate bot response and append it
        bot_response = assistant.get_response(user_message)
        history.append(ChatMessage(role="assistant", content=bot_response))
    return history, ""

# Gradio interface
with gr.Blocks() as ui:
    gr.Markdown("# 🤖 USTC AI Chatbot")
    chatbot = gr.Chatbot(type="messages", label="Chat")
    
    with gr.Row():
        user_input = gr.Textbox(placeholder="Ask something...", show_label=False, lines=1)
        send_button = gr.Button("➤", elem_id="send-btn")

    # Bind events for the input and button
    send_button.click(chat_with_bot, [chatbot, user_input], [chatbot, user_input])
    user_input.submit(chat_with_bot, [chatbot, user_input], [chatbot, user_input])

# Launch the app
if __name__ == "__main__":
    ui.launch()

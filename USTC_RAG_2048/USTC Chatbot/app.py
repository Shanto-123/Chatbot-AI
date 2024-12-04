from utils.assistant import UniversityAssistant
from dotenv import load_dotenv
import gradio as gr

# Load environment variables and initialize the assistant
load_dotenv()
assistant = UniversityAssistant(index_name="ustc-rag-2048")

# Define the chatbot function
def chat_with_bot(user_message):
    if user_message.strip():
  
        response = assistant.get_response(user_message)
        return response
    return "I couldn't understand that. Can you please rephrase?"

# Create the Gradio interface
with gr.Blocks(css="""
    body {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f5f6f7;
        color: #333;
    }
    .gradio-container {
        max-width: 600px;
        margin: 20px auto;
        background-color: #ffffff;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        height: 80vh;
    }
    .gr-header {
        background-color: lime;
        color: white;
        padding: 20px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .gr-header h1 {
        margin: 0;
        font-weight: bold;
    }
    .gr-chatbot {
        background-color: #f1f1f1;
        padding: 20px;
        height: calc(100% - 80px);
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }
    .gr-message {
        display: flex;
        gap: 10px;
        align-items: flex-start;
        max-width: 80%;
    }
    .gr-message.user {
        flex-direction: row-reverse;
    }
    .gr-message.user .gr-avatar {
        background-color: #0078FF;
        color: white;
    }
    .gr-message.assistant .gr-avatar {
        background-color: #e1e4e8;
        color: #0078FF;
    }
    .gr-avatar {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        font-size: 18px;
        font-weight: bold;
    }
    .gr-bubble {
        background-color: #ffffff;
        padding: 12px 15px;
        border-radius: 18px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        font-size: 16px;
        color: #333;
        word-wrap: break-word;
        white-space: pre-wrap;
        max-width: 80%;
    }
    .gr-message.user .gr-bubble {
        background-color: #0078FF;
        color: white;
    }
    .gr-message.assistant .gr-bubble {
        background-color: #e1e4e8;
        color: #333;
    }
    .gr-footer {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px 20px;
        background-color: #ffffff;
        border-top: 1px solid #eaeaea;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
    }
    .gr-textbox {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .gr-textbox textarea {
        flex-grow: 1;
        border: 1px solid #e5e5e5;
        border-radius: 20px;
        padding: 12px;
        font-size: 16px;
        color: #333;
        background-color: #f1f1f1;
    }
    .gr-textbox textarea:focus {
        outline: none;
        border-color: #0078FF;
    }
    .gr-button {
        weight : 10px
        background-color: #0078FF;
        color: white;
        border-radius: 50%;
        font-size: 24px;
        font-weight: bold;
        width: 50px;
        height: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: background-color 0.2s, box-shadow 0.2s;
        border: none;
    }
    .gr-button:hover {
        background-color: #005bb5;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);

    .small-button {
        width: 10px;  /* Adjust width as needed */
        height: 30px; /* Adjust height as needed */
        font-size: 12px; /* Adjust font size as needed */
        }

    .gr-textbox textarea {
    flex-grow: 1;
    border: 1px solid #e5e5e5;
    border-radius: 20px;
    padding: 12px;
    font-size: 16px;
    color: #333;
    background-color: #f1f1f1;
    min-height: 40px; /* Adjust as needed for a good proportion */
}

.gr-button {
    background-color: #0078FF;
    color: white;
    border-radius: 50%;
    font-size: 24px;
    font-weight: bold;
    width: 50px; /* Explicit size for the button */
    height: 50px; /* Explicit size for the button */
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: background-color 0.2s, box-shadow 0.2s;
    border: none;
}

.gr-button:hover {
    background-color: #005bb5;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

    }
""") as ui:
    # Add header with the USTC logo and the title in bold
    gr.HTML("""
    <div class="gr-header">
        <img src="https://i.ibb.co.com/JCFLXwB/image.png" style="width: 40px; height: auto; margin-right: 10px;">
        <h1>USTC AI-Powered Chatbot </h1>
    </div>
    """)

    # Chatbot interface
    chatbot = gr.Chatbot(label="Chat", type="messages")
    
    # Input area with a footer (aligned horizontally)
    with gr.Row(
        # ="panel"
        ):
        with gr.Column(scale=90):
            user_input = gr.Textbox(label="", placeholder="Ask something...", lines=1, interactive=True)
            send_button = gr.Button("Send ➤", size = "lg")  # Send button as a circle with an arrow icon
    
    # Function to update chat
    def update_chatbot(user_message, history):
        if user_message:
            history.append({"role": "user", "content": f" {user_message} 👤"})  # Add user message
            bot_response = chat_with_bot(user_message)
            history.append({"role": "assistant", "content": f"🤖 {bot_response}"})  # Add bot response
        return history, ""

    send_button.click(update_chatbot, [user_input, chatbot], [chatbot, user_input])
    user_input.submit(update_chatbot, [user_input, chatbot], [chatbot, user_input])

# Launch the Gradio app
if __name__ == "__main__":
    ui.launch()

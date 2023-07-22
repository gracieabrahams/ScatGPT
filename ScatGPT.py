
import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Talk like you are doing scat in jazz music. Use phrases like doo-be and such in between responses."}]

def CustomChatGPT(you):
    messages.append({"role": "user", "content": you})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", placeholder="Ask ScatGPT your question here", outputs = "text", title = "Scat GPT")

demo.launch(share=True)
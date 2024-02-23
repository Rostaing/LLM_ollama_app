import streamlit as st
import ollama
import time
# ollama pull llama2

def stream_data(text, delay:float=0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)

def llm_model():
    prompt = st.chat_input("Ask anything")

    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
            
        
        with st.spinner("Progess..."):
            result = ollama.chat(model="llama2", messages=[{"role":"user", "content":prompt}])
            response = result["message"]["content"]
            st.write_stream(stream_data(response))

def main():
    llm_model()

if __name__ == "__main__":
    main()
    
    
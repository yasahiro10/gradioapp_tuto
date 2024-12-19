#create an interface with text takes input and return hello input
import gradio as gr
#running on localhost:7860
def get_name_with_hello(name:str)->str:
    return 'hello'+name
if __name__ == '__main__':
    demo =gr.Interface(fn=get_name_with_hello,inputs='text',outputs='text')
    demo.launch()
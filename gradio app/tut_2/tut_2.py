import gradio as gr
def get_hello_with_name(name:str)->str:
    return 'Hello'+ name + '!'
#you check logs by clicking in the flag bottom to see the
if __name__ == '__main__':
    demo = gr.Interface(fn=get_hello_with_name,inputs=gr.Textbox(lines=3),outputs='text')
    demo.launch()
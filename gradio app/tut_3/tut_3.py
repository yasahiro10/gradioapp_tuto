import gradio as gr
#interface with checkbox
def return_summary(name:str,temperature:int,is_morning:bool)->str:
    return_value =  f'Hello {name} ! It is {temperature} degree today'
    if is_morning:
        return_value+='and it"s morning'
    return return_value

if __name__ == '__main__':
    demo = gr.Interface(fn=return_summary,inputs=['text',gr.Slider(0,100),'checkbox'],outputs='text')
    demo.launch()
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=[gr.Text(), "text"],
    outputs=["text"],
)

demo.launch()

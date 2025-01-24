# set api key

# export TOGETHER_API_KEY=<api-key>
from together import Together


client = Together()

def chat(query):
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        messages=[
            {
                "role": "user",
                "content": query
            }
    ],
        max_tokens=None,
        temperature=0.1,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<eos>","<end_of_turn>"],
        #stream=True
    )
    return response.choices[0].message.content

#print(chat("quien es sam altman?"))
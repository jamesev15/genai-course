# colocar en el terminal la variable de entorno
# export TAVILY_API_KEY=<api-key>

import requests
import os

tavily_url = "https://api.tavily.com/search"
headers = {"Content-Type": "application/json"}


def get_info(query):
    data = {
        "api_key": os.getenv("TAVILY_API_KEY"),
        "query": query,
    }

    response = requests.post(
        url=tavily_url,
        headers=headers,
        json=data
    )

    # print(response.status_code)
    response = response.json()

    resumen = ""

    for result in response["results"]:
        resumen = resumen + result["content"] + "\n"

    return resumen

query = input("introduce tu query: ")
print(get_info(query))
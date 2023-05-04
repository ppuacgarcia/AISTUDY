import os
import openai

def ResponsePdf(txt):
    openai.api_key = "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"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=txt,
    temperature=0.4,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print("==========================================")
    print(response.choices[0].text)
    return response.choices[0].text
ResponsePdf("QUIEN ES EL AUTOR  de este pdf: http://biblio3.url.edu.gt/Libros/put_tris.pdf")

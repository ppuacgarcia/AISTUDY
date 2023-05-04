#import os
#import openai

 #def ResponsePdf(self,txt):
    #    openai.api_key = "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"
    #    response = openai.Completion.create(
    #    model="text-davinci-001",
    #    prompt=txt,
    #    temperature=0.4,
    #    max_tokens=128,
    #    top_p=1,
    #    frequency_penalty=0,
    #    presence_penalty=0
    #    )
    #    print(response.choices[0].text)
    #    return response.choices[0].text
def separar(txt):
    return txt.split("\n")
def correcto(res,pos):
    if res.find("C:")!=-1:
        respuesta=res.replace('C:', '')
        return [respuesta,pos]
    else:
        respuesta=res.replace('I:', '')
        return [respuesta,-1]
texto="¿Cuál es el enfoque principal del libro El Put Tris: Una etnografía sobre la vida cotidiana en un barrio popular de la ciudad de Guatemala?\nA) C: Análisis de la dinámica del mercado en la ciudad de Guatemala\nB) I: Investigación sobre la industria turística de Guatemala\nC) I: Estudio sobre la evolución política del país\n D) I: Análisis económico de la ciudad de Guatemala."
preguntas=separar(texto)[0]
respuestas=[]
respuestas=[separar(texto)[1],separar(texto)[2],separar(texto)[3]]
PCorrecta=-1
for i in range (0,3):
  respuestas[i]=correcto(respuestas[i],i)[0]
  if(correcto(respuestas[i],i)[1]!=(-1)):
    PCorrecta=i

print("pregunta:"+preguntas)
print("respuesta 1:"+respuestas[0])
print("respuesta 2:"+respuestas[1])
print("respuesta 3:"+respuestas[2])    
print("la respuesta correcta es"+str(PCorrecta))    

import openai
import config
import sys
import pandas as pd
from time import sleep


def responderPregunta(nro_pregunta, data_frame, prompt_base): #la función toma el id de pregunta, le agrega el prompt base adelante y lo envía a chatgpt, luego guarda esa respuesta en el df y los tokens usados.
    
    #captura la pregunta del df con el nro pregunta
    pregunta = data_frame.loc[nro_pregunta, 'pregunta'] + '  ' + data_frame.loc[nro_pregunta, 'descripcion']
    
    #le sumo la pregunta al prompt
    prompt = prompt_base + "'" +str(pregunta) + "'" 
    
    #le paso a la lista de mensajes el mensaje del usuario, para que siga la conversación le voy concatenando el mensaje.
    messages.append({"role":"user", "content": prompt})

    #llamo a la api, llamando a create ()
    response = openai.ChatCompletion.create(model=model, messages=messages)
        
    #actualizo la cantidad de tokens
    cant_tokens = response.usage.total_tokens

    #guardo el mensaje
    response_text = response.choices[0].message.content 

    #Guardo prompt y respuesta en el df
    data_frame.loc[nro_pregunta, 'Prompt_Chat'] = prompt 
    data_frame.loc[nro_pregunta, 'Respuesta_Chat'] = response_text
    data_frame.loc[nro_pregunta, 'cant_tokens'] = cant_tokens

    return data_frame, response_text, cant_tokens



sys.stdout.reconfigure(encoding="utf-8")
#seteo la api key desde config
openai.api_key = config.api_key
model = "gpt-3.5-turbo"

#con el role system le damos contexto de cómo queremos que el chatGpt se comporte, se puede detallar lo que queramos.
context = {"role": "system",
             "content": "eres un chatbot amable y servicial"

}

messages = [context]

#Levanto el archivo con las preguntas a chatGPT
preguntas_chatgpt = 'preguntas_chatgpt.xlsx'
df = pd.read_excel(preguntas_chatgpt)

df = df.fillna('')

#defino el prompt base que irá antes de las preguntas. 
prompt_base = """eres un experto en comercio exterior europeo, con un magister en certificaciones OEA (Operador Económico Autorizado).
Estoy completando un cuestionario de auto Evaluación para preparar a mi empresa para certificarse.
Necesito que complementes la siguiente pregunta del formulario con información adicional útil y de calidad, que me de contexto de qué me están preguntando y cómo espera que se responda la pregunta
Por favor que la información sea concisa y aporte valor
Evita contestar información fuera de la pregunta (por ejemplo, que es una pregunta de un cuestionario)
pregunta: """



clase_pregunta=''
# Ciclar sobre cada fila del DataFrame
for index, row in df.iterrows():
    print("pregunta número: ", index)
    print(row[1])
    if clase_pregunta == row[1]: 
        print('sigue messeges')
    else:
        print('reinicia messeges')
        messages = [context]

    clase_pregunta = row[1]
    
    # Procesar la información y agregar una nueva columna
    if row[1] == 3 and row[0] == 1:
        responderPregunta(index, df, prompt_base)
        print('responde')
    else:
        print('No responde')
    #sleep(5)







#guardo en el excel
df.to_excel(preguntas_chatgpt, index=False)



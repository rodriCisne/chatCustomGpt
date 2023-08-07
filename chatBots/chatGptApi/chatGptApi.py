import openai
import config
import sys
import whisper


sys.stdout.reconfigure(encoding="utf-8")
#seteo la api key desde config
openai.api_key = config.api_key
model = "gpt-3.5-turbo"

#con el role system le damos contexto de cómo queremos que el chatGpt se comporte, se puede detallar lo que queramos.
context = {"role": "system",
             "content": "eres un chatbot amable y servicial"

}

messages = [context]

def process_question(messages, content):
    #le paso a la lista de mensajes el mensaje del usuario, para que siga la conversación le voy concatenando el mensaje.
    messages.append({"role":"user", "content": content})

    #llamo a la api, llamando a create ()
    response = openai.ChatCompletion.create(model=model,
                                messages=messages)
    
    #actualizo la cantidad de tokens
    cant_tokens = response.usage.total_tokens

    #guardo el mensaje
    response_text = response.choices[0].message.content 

    return response_text, cant_tokens



#acum_tokens = 0

def transcribe_audio(source):
    #prueba whisper
    model = whisper.load_model("base")
    return model.transcribe(source)["text"]



"""
while True:    

    #pregunta que para que responda el user
    content = input("¿Sobre qué quieres hablar?  ")

    #para salir del programa
    if content == "exit":
        break
    
    #si quiero iniciar una nueva conversación -> reseteo messages al contexto.
    if content == "new":
            print("🆕 Nueva conversación creada")
            messages = [context]
            continue
    
    #proceso la pregunta
    response_text, cant_tokens = process_question(messages, content)
    
    #actualizo la cantidad de tokens
    acum_tokens = acum_tokens + cant_tokens



    #imprimo mensaje
    print(response_text)
    #cant tokens
    print(f"Tokens: {cant_tokens}")
    print(f"Tokens acum: {acum_tokens}")


def showCommands():
    #mostrar comandos:
    def showCommands():
    #mostrar comandos:
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")
    table.add_row("/commands", "Muestra lista de comandos")
    print(table)
"""
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()


def executa_comando():
    try:
        with sr.Microphone() as source:
           
            print('Comandos: Nome - #Diz o nome da I.A, Toque - #Toca músicas no youtube, Pesquise por - #Faz um resumo do Wikipédia, Navegador - #Abre o navegador padrão da máquina, Clima - #Te alerta sobre o clima atual e da semana, Horas - #Te diz as horas atuais com base na sua localização, Sair - #Fecha o assistente virtual')
            print('Anakin, agora está te ouvindo!..')
            maquina.say('Anakin, agora está te ouvindo!')
            maquina.runAndWait()
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'Anakin' in comando:
                comando = comando.replace('Anakin', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Perdão, mas parece que algo está errado')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'pesquise por' in comando:
        procurar = comando.replace('pesquise por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Abrindo o Youtube e procurando sua música')
        maquina.runAndWait()
    
    elif 'navegador' in comando:
        navega = comando.replace('navegador', '')
        resultado = webbrowser.open('https://www.google.com.br/')
        maquina.say('Abrindo o seu navegador')
        maquina.runAndWait()

    elif 'sair' in comando:
        maquina.say('Desligando o Assistente virtual')
        maquina.runAndWait()
        exit()
        maquina.runAndWait()

    elif 'nome' in comando:
        maquina.say('Meu nome é Anakin, em homenagem a um personagem de Star Wars.')
        maquina.runAndWait()

    elif 'clima' in comando:
        clima = webbrowser.open('https://www.google.com.br/search?q=meu+clima&sxsrf=AJOqlzVoVjqY3O-tRzkS9pCBaHVWTWtfVg%3A1673690605409&source=hp&ei=7X3CY7LdFvnB5OUP14KdmAs&iflsig=AK50M_UAAAAAY8KL_dx0AU7fxBY42KWRigKQ7CFnAe2h&ved=0ahUKEwjyh_2v58b8AhX5ILkGHVdBB7MQ4dUDCAg&uact=5&oq=meu+clima&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQgAIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgcIABCABBAKMgUIABCABDoECCMQJzoUCC4QgAQQsQMQgwEQxwEQ0QMQ1AI6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoICAAQsQMQgwE6CAgAEIAEELEDOggILhCABBCxAzoECAAQA1AAWM0IYL8KaABwAHgAgAG0AogB1Q2SAQcwLjYuMi4xmAEAoAEB&sclient=gws-wiz')
        maquina.say('Procurando informações sobre o seu clima com base na sua localização atual')
        maquina.runAndWait()

    elif 'anotar' in comando:
        anotar = os.startfile('notepad.exe')
        maquina.runAndWait()

    

  






comando_voz_usuario()

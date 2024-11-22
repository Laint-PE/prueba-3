import discord
import os
import random
from discord.ext import commands

# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True

# Creación del bot
botprueba = commands.Bot(command_prefix="/", intents=intents)

# Evento al iniciar el bot
@botprueba.event
async def on_ready():
    print("¡Bot iniciado correctamente!")

# Comando para responder con un saludo
@botprueba.command()
async def hola(ctx):
    await ctx.send("¡Hola! ¿Cómo estás?")

# Comando para realizar una suma
@botprueba.command()
async def suma(ctx, num2: int, num3: int):
    resultado = num2 + num3
    await ctx.send(f"La suma de {num2} + {num3} es {resultado}.")

# Comando para realizar una división
@botprueba.command()
async def division(ctx, num2: int, num3: int):
    if num3 == 0:
        await ctx.send("Error: No se puede dividir entre 0.")
    else:
        resultado = num2 / num3
        await ctx.send(f"La división de {num2} / {num3} es {resultado}.")

# Comando para enviar un meme
@botprueba.command()
async def meme(ctx):
    # Variable que almacena los nombres de los archivos en la carpeta
    carpeta_memes = "PROYECTO2 CHATBOT/images"
    if os.path.exists(carpeta_memes):
        nombres_archivos = os.listdir(carpeta_memes)  # Obtiene la lista de archivos
        if nombres_archivos:
            # Variable que selecciona un archivo aleatorio
            archivo_aleatorio = random.choice(nombres_archivos)
            ruta_completa = os.path.join(carpeta_memes, archivo_aleatorio)
            
            # Envía el archivo seleccionado
            with open(ruta_completa, 'rb') as f:
                imagen = discord.File(f)
            await ctx.send(file=imagen)
        else:
            await ctx.send("La carpeta de memes está vacía.")
    else:
        await ctx.send("No se encontró la carpeta de memes.")

# Comando para fomentar el reciclaje
@botprueba.command()
async def reciclaje(ctx):
    await ctx.send("Recicla, por favor. ¡El planeta lo necesita!")


botprueba.run("MTI5Njk2ODM1NTM5OTM0MDEzMw.GAO-Bx.gxgkmA8WfQgHpnTlaesu1dZFYlU7n4oyFej9Lo")  

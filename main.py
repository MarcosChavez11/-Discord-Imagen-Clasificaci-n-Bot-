import discord
import random, os, requests
from discord.ext import commands
from bot_logic import gen_pass, flip_coin, gen_emodji, numero
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="+", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command(name="hola")
async def hola(ctx):
    await ctx.send("Hola")

@bot.command(name="bye")
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command(name="emoji")
async def emoji(ctx):
    await ctx.send(gen_emodji())

@bot.command(name="coin")
async def coin(ctx):
    await ctx.send(flip_coin())
import random

@bot.command(name="azar")
async def azar(ctx):
    numero = random.randint(1, 100)
    await ctx.send(f"Tu número aleatorio es: {numero}")

@bot.command(name="repite")
async def repite(ctx, veces: int, *, contenido: str = "repitiendo..."):
    for _ in range(veces):
        await ctx.send(contenido)

@bot.command(name="joined")
async def joined(ctx, member: discord.Member):
    if member.joined_at:
        joined_date = discord.utils.format_dt(member.joined_at, style="F")
        await ctx.send(f'{member.name} se unió el {joined_date}')
    else:
        await ctx.send(f"No se pudo determinar cuándo {member.name} se unió.")

@bot.command(name="pswd")
async def pswd(ctx):
    await ctx.send(f"Tu contraseña generada es: {gen_pass(10)}")

@bot.command(name="suma")
async def suma(ctx, a: int = None, b: int = None):  # Hacemos los argumentos opcionales
    if a is None or b is None:  
        await ctx.send("Error: Debes ingresar dos números. Ejemplo: `+suma 5 10`")
        return
    await ctx.send(f"La suma de {a} + {b} es {a + b}")

@bot.command(name="dado")
async def dado(ctx):
    resultado = random.randint(1, 6)
    await ctx.send(f"🎲 Has sacado un {resultado}")

#@bot.command()
#async def memeprogramacion(ctx):
    #x= os.listdir("imageprogramacion")
    #y= random.choice(x)
    #with open(f'imageprogramacion/{y}', 'rb') as f:
        #picture = discord.File(f)
    #await ctx.send(file=picture)

#@bot.command()
#async def memepov(ctx):
    #x= os.listdir("imagepov")
    #y= random.choice(x)
    #with open(f'imagepov/{y}', 'rb') as f:
        #picture = discord.File(f)
    #await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data.get('url', None)
    return None  

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data.get('url', None)
    return None  

def get_pokemon_image_url():
    pokemon_id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data["sprites"]["front_default"]
    return None  

def get_anime_by_keyword(keyword):
    url = f"https://kitsu.io/api/edge/anime?filter[text]={keyword}"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data.get('image', None)
    return None  

@bot.command(name="duck")
async def duck(ctx):
    image_url = get_duck_image_url()
    if image_url:
        await ctx.send("🦆 ¡Aquí tienes un pato! 🦆")
        await ctx.send(image_url)
    else:
        await ctx.send("No se pudo obtener la imagen del pato. Intenta de nuevo.")

@bot.command(name="dog")
async def dog(ctx):
    image_url = get_dog_image_url()
    if image_url:
        await ctx.send("🐶 ¡Aquí tienes un perrito! 🐶")
        await ctx.send(image_url)
    else:
        await ctx.send("No se pudo obtener la imagen del perro. Intenta de nuevo.")

@bot.command(name="pokemon")
async def pokemon(ctx):
    '''Envía la imagen de un Pokémon aleatorio desde la PokeAPI'''
    pokemon_id = random.randint(1, 1017)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    res = requests.get(url)
    if res.status_code != 200:
        await ctx.send("No se pudo obtener la imagen del Pokémon. Intenta de nuevo.")
        return
    data = res.json()
    nombre = data['name'].capitalize()
    imagen_url = data['sprites']['other']['official-artwork']['front_default']
    await ctx.send(f"¡Aquí tienes un Pokémon aleatorio! 🐉\n**{nombre}**")
    await ctx.send(imagen_url)

@bot.command(name="anime")
async def anime(ctx, *, keyword: str):
    '''Busca animes relacionados con cualquier palabra clave que el usuario proporcione.'''
    animes = get_anime_by_keyword(keyword)
    if animes:
        # Enviar todos los resultados
        for anime in animes:
            title = anime['attributes']['canonicalTitle']
            description = anime['attributes'].get('description', 'No description available')
            await ctx.send(f"**{title}**\n{description}\n")
    else:
        await ctx.send(f"No se encontraron animes con la palabra '{keyword}'. Intenta de nuevo.")

@bot.command(name="fox")
async def fox(ctx):
    image_url = get_fox_image_url()
    if image_url:
        await ctx.send("🦊 ¡Aquí tienes un zorro! 🦊")
        await ctx.send(image_url)
    else:
        await ctx.send("No se pudo obtener la imagen del zorro. Intenta de nuevo.")


@bot.command(name="chiste")
async def chiste(ctx):
    chistes = [
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas.",
        "¿Cómo se dice pañuelo en chino? Saka-moko.",
    ]
    await ctx.send(random.choice(chistes))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command(name="clasificar")
async def clasificar(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre = archivo.filename
            url = archivo.url
            await archivo.save(nombre)
            await Mctx.send(f"la imagen {nombre} se ha guardado")
        try:
            clase = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=nombre)
            await ctx.send(clase)

            if clase[0] == "Aguacate":
                await ctx.send("El aguacate es una fuente rica en vitaminas K, E, C, B6, ácido fólico y potasio. Se cultiva principalmente en México, Colombia, Perú y Estados Unidos (California). Su mayor consumo está en México, Estados Unidos y España. Se puede comer en guacamole, ensaladas, sopas frías como el gazpacho, tostadas o batidos. Contiene alrededor de 160 calorías por cada 100 gramos, con 2 g de proteína, 15 g de grasa (grasas monoinsaturadas beneficiosas), 9 g de carbohidratos y 7 g de fibra. Sus beneficios incluyen mejorar el colesterol, favorecer la salud del corazón, ayudar a absorber otras vitaminas y ser bueno para la piel y el sistema inmunológico.")
            elif clase[0] == "Arandano":
                await ctx.send("Los arándanos son ricos en vitamina C, vitamina K, manganeso y antioxidantes como las antocianinas. Se cultivan principalmente en Canadá, Estados Unidos y Chile. Su mayor consumo se da en Estados Unidos y países nórdicos de Europa. Se consumen en batidos, mermeladas, postres, yogures o directamente frescos. Contienen unos 57 kcal por 100 g, con 0.7 g de proteína, 0.3 g de grasa, 14 g de carbohidratos y 2.4 g de fibra. Ayudan a mejorar la memoria, fortalecer el sistema inmunológico, cuidar la visión y prevenir enfermedades crónicas gracias a sus poderosos antioxidantes.")
            elif clase[0] == "Banana":
                await ctx.send("La banana contiene vitamina C, B6, potasio y magnesio. Se cultiva ampliamente en Ecuador, India, Brasil y Filipinas. Su mayor consumo está en América Latina, África y Asia. Puede comerse natural, en batidos, licuados, plátano frito o en postres. Tiene alrededor de 89 kcal por 100 g, con 1.1 g de proteína, 0.3 g de grasa, 23 g de carbohidratos y 2.6 g de fibra. Ayuda a mantener niveles normales de presión arterial, mejora la función muscular, aporta energía rápida y favorece la salud digestiva.")
            elif clase[0] == "Cereza":
                await ctx.send("Las cerezas contienen vitaminas A, C, E, potasio y antioxidantes como la melatonina. Se cultivan especialmente en Turquía, Estados Unidos e Italia. Su mayor consumo está en EE.UU., Europa del Este y Turquía. Se pueden comer frescas, en postres, tartas, mermeladas o incluso en cócteles. Por cada 100 g tienen alrededor de 50 kcal, con 1 g de proteína, 0.3 g de grasa, 12 g de carbohidratos y 2 g de fibra. Ayudan a mejorar el sueño, reducir la inflamación, favorecer la recuperación muscular después del ejercicio y fortalecer el sistema inmunológico.")
            elif clase[0] == "Frambuesa":
                await ctx.send("Las frambuesas son ricas en vitamina C, vitamina K, antioxidantes y fibra. Se cultivan mucho en Rusia, México y Estados Unidos. Su mayor consumo está en Europa y Estados Unidos. Se comen frescas, en postres, yogures, batidos o como parte de salsas dulces. Tienen aproximadamente 52 kcal por cada 100 g, con 1.2 g de proteína, 0.7 g de grasa, 12 g de carbohidratos y 6.5 g de fibra. Estas frutas mejoran la salud digestiva, son antiinflamatorias, apoyan la salud del corazón y ayudan a controlar los niveles de azúcar en sangre.")
            elif clase[0] == "Fresa":
                await ctx.send("La fresa es rica en vitamina C, manganeso, antioxidantes y flavonoides. Se cultiva principalmente en Estados Unidos, México y España. Su mayor consumo también está en Estados Unidos, Europa y Japón. Se puede comer fresca, en postres, batidos, helados o como acompañamiento en platos dulces. Por cada 100 g contiene unos 32 kcal, 0.7 g de proteína, 0.3 g de grasa, 8 g de carbohidratos y 2 g de fibra. Las fresas ayudan a prevenir enfermedades cardiovasculares, mejoran la salud de la piel y refuerzan el sistema inmunológico.")
            elif clase[0] == "Guayaba":
                await ctx.send("La guayaba destaca por su alto contenido de vitamina C, además de vitamina A, potasio y fibra. Se cultiva mucho en México, Brasil, Colombia y la India. Su mayor consumo se da en Latinoamérica, India y partes de Asia. Se puede comer fresca, en jugos, mermeladas o postres. Tiene alrededor de 68 kcal por cada 100 g, 2.6 g de proteína, 0.6 g de grasa, 14 g de carbohidratos y 5.4 g de fibra. Mejora la salud digestiva, fortalece el sistema inmunológico, ayuda a controlar la diabetes y promueve la salud de la piel.")
            elif clase[0] == "Kiwi":
                await ctx.send("El kiwi es muy rico en vitamina C, vitamina K, vitamina E, potasio y fibra. Se cultiva sobre todo en Nueva Zelanda, Italia y China. Su mayor consumo se da en Europa, Estados Unidos y Japón. Se come fresco, en ensaladas, batidos o como aderezo en postres. Tiene cerca de 61 kcal por cada 100 g, 1.1 g de proteína, 0.5 g de grasa, 15 g de carbohidratos y 3 g de fibra. El kiwi mejora la digestión, fortalece el sistema inmunológico, favorece la salud cardiovascular y ayuda a mejorar la calidad del sueño.")
            elif clase[0] == "Mandarina":
                await ctx.send("La mandarina es rica en vitamina C, vitamina A, folatos y antioxidantes. Se cultiva principalmente en China, España y Turquía. Su mayor consumo está en China, Estados Unidos y Europa. Se puede comer fresca, en postres, jugos o como parte de recetas saladas. Contiene alrededor de 53 kcal por cada 100 g, 0.8 g de proteína, 0.3 g de grasa, 13 g de carbohidratos y 1.8 g de fibra. Ayuda a fortalecer el sistema inmunológico, mejora la visión y la piel, y favorece la salud del corazón.")
            elif clase[0] == "Mango":
                await ctx.send("El mango contiene vitaminas A, C, E, B6, potasio y fibra. Se cultiva principalmente en India, China y México. Su mayor consumo está en India, Asia y América Latina. Se puede comer fresco, en jugos, batidos, postres o ensaladas tropicales. Tiene alrededor de 60 kcal por cada 100 g, 0.8 g de proteína, 0.4 g de grasa, 15 g de carbohidratos y 1.6 g de fibra. Mejora la salud de la piel, favorece la vista, fortalece el sistema inmunológico y ayuda al buen funcionamiento del sistema digestivo.")
            elif clase[0] == "Manzana":
                await ctx.send("La manzana es rica en vitamina C, fibra, antioxidantes y polifenoles. Se cultiva en gran parte del mundo, siendo China, Estados Unidos y Polonia grandes productores. Su mayor consumo está en Europa, Estados Unidos y China. Se puede comer fresca, horneada, en jugos, compotas, tartas o como ingrediente en platos dulces y salados. Contiene unos 52 kcal por cada 100 g, 0.3 g de proteína, 0.2 g de grasa, 14 g de carbohidratos y 2.4 g de fibra. Es buena para el corazón, ayuda a regular el azúcar en sangre, mejora la salud digestiva y fortalece el sistema inmunológico.")
            elif clase[0] == "Melon":
                await ctx.send("El melón contiene vitamina A, vitamina C, potasio y agua en grandes cantidades. Se cultiva mucho en China, Turquía, Irán y Estados Unidos. Su mayor consumo está en Oriente Medio, América Latina y Asia. Se come fresco, en ensaladas de frutas, batidos o como postre refrescante. Tiene alrededor de 34 kcal por cada 100 g, 0.8 g de proteína, 0.1 g de grasa, 8 g de carbohidratos y 0.9 g de fibra. Hidrata, favorece la salud ocular, es baja en calorías y ayuda a mantener la piel saludable.")
            elif clase[0] == "Mora":
                await ctx.send("La mora es rica en vitamina C, vitamina K, antioxidantes y fibra. Se cultiva mucho en México, Estados Unidos y Serbia. Su mayor consumo está en Estados Unidos, Europa y Canadá. Se puede comer fresca, en postres, mermeladas, batidos o como parte de desayunos. Tiene alrededor de 43 kcal por cada 100 g, 1.4 g de proteína, 0.7 g de grasa, 10 g de carbohidratos y 5.3 g de fibra. Mejora la salud digestiva, combate el estrés oxidativo, ayuda a prevenir enfermedades cardiovasculares y fortalece el sistema inmunológico.")
            elif clase[0] == "Naranja":
                await ctx.send("La naranja es muy rica en vitamina C, vitamina A, flavonoides y fibra. Se cultiva principalmente en Brasil, Estados Unidos (Florida), China y España. Su mayor consumo está en Estados Unidos, Europa y Brasil. Se puede comer fresca, en jugos naturales, postres o como parte de platos salados. Contiene alrededor de 47 kcal por cada 100 g, 0.9 g de proteína, 0.1 g de grasa, 12 g de carbohidratos y 2.4 g de fibra. Fortalece el sistema inmunológico, mejora la salud de la piel, ayuda a absorber hierro y es beneficiosa para el corazón.")
            elif clase[0] == "Papaya":
                await ctx.send("La papaya contiene vitamina A, vitamina C, folatos, enzimas digestivas (como la papaina) y antioxidantes. Se cultiva mucho en India, Brasil, México y Nigeria. Su mayor consumo está en América Latina, Asia y África. Se puede comer fresca, en jugos, batidos o como parte de platos exóticos. Tiene alrededor de 43 kcal por cada 100 g, 0.5 g de proteína, 0.3 g de grasa, 11 g de carbohidratos y 2.5 g de fibra. Mejora la digestión, fortalece el sistema inmunológico, favorece la salud de la piel y ayuda a combatir la inflamación.")
            elif clase[0] == "Pera":
                await ctx.send("La pera contiene vitamina C, vitamina K, cobre y fibra soluble. Se cultiva principalmente en China, Estados Unidos, Argentina y Chile. Su mayor consumo está en Europa, Estados Unidos y Asia. Se puede comer fresca, horneada, en ensaladas o como parte de postres. Tiene alrededor de 57 kcal por cada 100 g, 0.4 g de proteína, 0.1 g de grasa, 15 g de carbohidratos y 3.1 g de fibra. Es buena para el corazón, mejora la digestión y favorece la salud ósea gracias a su contenido de vitamina K.")
            elif clase[0] == "Pina":
                await ctx.send("La piña es rica en vitamina C, manganeso, bromelina (una enzima digestiva) y antioxidantes. Se cultiva principalmente en Filipinas, Brasil, Costa Rica e Indonesia. Su mayor consumo está en Estados Unidos, América Latina y Asia. Se puede comer fresca, en jugos, batidos, ensaladas o como parte de platos tropicales. Contiene alrededor de 50 kcal por cada 100 g, 0.5 g de proteína, 0.1 g de grasa, 13 g de carbohidratos y 1.4 g de fibra. Mejora la digestión, reduce la inflamación, fortalece el sistema inmunológico y favorece la salud de la piel.")
            elif clase[0] == "Pitahaya":
                await ctx.send("La pitahaya contiene vitamina C, hierro, magnesio, fibra y antioxidantes como las betacianinas. Se cultiva principalmente en Vietnam, Nicaragua, Israel y México. Su mayor consumo está en Asia, Estados Unidos y países latinoamericanos. Se puede comer fresca, en batidos, smoothies o como decoración en postres. Tiene alrededor de 60 kcal por cada 100 g, 1.2 g de proteína, 0.6 g de grasa, 13 g de carbohidratos y 3 g de fibra. Mejora la salud digestiva, combate el estrés oxidativo, fortalece el sistema inmunológico y ayuda a mantener una piel saludable.")
            elif clase[0] == "Sandia":
                await ctx.send("La sandía es rica en vitamina A, vitamina C, licopeno (antioxidante) y agua. Se cultiva mucho en China, Turquía, Estados Unidos e Irán. Su mayor consumo está en Estados Unidos, Oriente Medio y Asia. Se come fresca, en jugos, batidos o como postre refrescante. Tiene alrededor de 30 kcal por cada 100 g, 0.6 g de proteína, 0.2 g de grasa, 8 g de carbohidratos y 0.4 g de fibra. Es altamente hidratante, mejora la salud de la piel, favorece la salud del corazón y ayuda a prevenir ciertos tipos de cáncer gracias al licopeno.")
            elif clase[0] == "Tomate":
                await ctx.send("Aunque técnicamente es una fruta, el tomate es consumido como hortaliza. Contiene vitamina C, vitamina K, potasio, licopeno y antioxidantes. Se cultiva en muchos países, siendo China, India y Estados Unidos grandes productores. Su mayor consumo está en Europa, Estados Unidos, América Latina y Asia. Se puede comer fresco, cocido, en salsas, sopas, ensaladas o jugos. Tiene alrededor de 18 kcal por cada 100 g, 0.9 g de proteína, 0.2 g de grasa, 3.9 g de carbohidratos y 1.2 g de fibra. Mejora la salud del corazón, combate el estrés oxidativo, favorece la salud de la piel y ayuda a prevenir enfermedades degenerativas.")
            elif clase[0] == "Uva":
                await ctx.send("La uva contiene vitamina C, vitamina K, antioxidantes como el resveratrol y flavonoides. Se cultiva en gran parte del mundo, siendo Italia, China y Estados Unidos grandes productores. Su mayor consumo está en Europa, Estados Unidos y Asia. Se puede comer fresca, en jugos, vinos, geles o como parte de postres. Tiene alrededor de 69 kcal por cada 100 g, 0.7 g de proteína, 0.2 g de grasa, 18 g de carbohidratos y 0.9 g de fibra. Favorece la salud del corazón, mejora la circulación, combate el envejecimiento celular y fortalece el sistema inmunológico.")
        except:
            await ctx.send("No se pudo analizar el archivo, recuerda solo subir imágenes en PNG, JPG y JPEG")
        

    else:
        await ctx.send("No hay archivos adjuntos")

bot.run("")
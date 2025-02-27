    import requests
    from datetime import datetime, timedelta

    # API de la NASA
    NASA_API_URL = "https://api.nasa.gov/planetary/apod"
    NASA_API_KEY = "jpz4g89X4R79vYjueprMEB8imeCSPJHLunYJnhR2"  #Clave individual para acceder a la API de la NASA

    # API de Pokémon
    POKE_API_URL = "https://pokeapi.co/api/v2/pokemon/"

    def obtener_foto_nasa(fecha):
        """Consulta la API de la NASA y obtiene la imagen de la fecha ingresada"""
        while True:
            params = {"api_key": NASA_API_KEY, "date": fecha}
            response = requests.get(NASA_API_URL, params=params)  # Método GET para obtener datos

            if response.status_code == 200:
                data = response.json()
                print(f"\n📅 Fecha: {fecha}")
                print(f"🖼️ Foto: {data.get('title', 'Sin titulo')}")
                print(f"📸 Imagen: {data.get('url', 'No disponible')}\n")
                break
            else:
                print(f"❌ No se encontro imagen para {fecha}, probando un dia antes...")
                fecha = (datetime.strptime(fecha, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")

    def obtener_info_pokemon(nombre):
        """Consulta la API de Pokemon y obtiene nombre, habilidades, estadisticas y movimientos"""
        url = POKE_API_URL + nombre.lower()
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            nombre_pokemon = data["name"].capitalize()
            habilidades = [habilidad["ability"]["name"].capitalize() for habilidad in data["abilities"]]
            estadisticas = {stat["stat"]["name"].capitalize(): stat["base_stat"] for stat in data["stats"]}
            movimientos = [mov["move"]["name"].capitalize() for mov in data["moves"][:5]]  # Solo los primeros 5 movimientos

            print(f"\n🐉 Pokemon: {nombre_pokemon}")
            print(f"🎯 Habilidades: {', '.join(habilidades)}")
            print("📊 Estadísticas:")
            for stat, valor in estadisticas.items():
                print(f"    🔥{stat}: {valor}") #se le pusieron emogis para que se viera mas bonito
            print(f"🌀 Movimientos: {', '.join(movimientos)}\n")

        else:
            print("\n❌ Pokemon no encontrado. Intenta con otro nombre.\n")

    def main():
        while True:
            opcion = input("📡 NASA (A) o 🐾 Pokemon (P): ").strip().upper()

            if opcion == "A":
                dia = input("Día (DD): ")
                mes = input("Mes (MM): ")
                año = input("Año (YYYY): ")
                fecha = f"{año}-{mes}-{dia}"
                obtener_foto_nasa(fecha)
            #Segun esto es como la mezcla de If y Else
            elif opcion == "P":
                pokemon = input("Ingrese el nombre del Pokemon: ").strip().lower()
                obtener_info_pokemon(pokemon)

            else:
                print("⚠️ Opcion no valida. Elige 'A' para NASA o 'P' para Pokemon.")

            otra_busqueda = input("¿Hacer otra busqueda? (s/n): ").strip().lower()
            if otra_busqueda != 's':
                print("¡Hasta luego! 🚀")
                break

    if __name__ == "__main__":
        main()

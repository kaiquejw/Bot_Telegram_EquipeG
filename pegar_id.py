import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu8BjA0mP3LhnQEHqXuIpmENfbmh9AAokCzgsVrcw0ukDuSUZZsXbLPI6eNHFjYI-_e7kdjBX55XSxJIZORu57KXc0F9F_-na8-tEcxz2rh817gc-T5z5U_B6zQEv_faK-QNpmng4MV8bEwXcrzqtox1eaJlyLZmjF-UnwmFr9fmAkJym-NXScqg0HOOuwgTdHeHY4c7cHz6pg_CYdOAizXILqsiEoErwOILZtE28MdX4NedSau-apUIcE7R6v_M9pU4KMWKZJXOsV7YIZroK3ivQQrALzzce_uzXvL8s2i4pC9Vpqp7WHo6OjryA2LRN9BrJQVrJLMxjmNR54UWIsck='

async def main():
    print("Conectando...")
    client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
    await client.connect()
    
    print("\n👇 AQUI ESTÃO SEUS ÚLTIMOS GRUPOS/CONVERSAS 👇\n")
    print(f"{'NOME DO GRUPO':<30} | {'ID PARA O GITHUB'}")
    print("-" * 50)
    
    # Pega as últimas 15 conversas
    async for dialog in client.iter_dialogs(limit=15):
        print(f"{dialog.name:<30} | {dialog.id}")
        
    print("\n👆 Copie o ID (número negativo) do grupo 'Teste' e coloque no GitHub.\n")

if __name__ == '__main__':
    asyncio.run(main())
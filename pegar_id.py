import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuxC3NeIYl9SnqU8j8NPbKT9MzcWJHesMcne6SK9ZtCqKc1wx7BBBG_vdtH2pfbwgO29Uhe6oCiBKOIY3UcCDpgstlUs4vW_0Ub2JMCMMrC7MSsQuHPn4qyhMCXOuVzfdItP1qsOHGWKJTVbxvQZg3LHZUnX4mV0f4jWHipLs8FA6l8AQl28_1uvaZ2cejfKG9E0aLiHmeWIBJBMxdQ6M4gYdGcXTCKWdj3MR3_MqKwt1fVZw6CIR2CC5_eWcE89kowS6q8qL0YKbwpYqOulBxFz5ReSvvQA8X-k7ku9RUzbG91subHZX9h-FM3hl6e4VjDsGbMJpPK_t3lfl0vSW2Sk='

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
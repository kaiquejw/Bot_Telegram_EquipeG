import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzQBu0iE1BM-X44QA9q2JPF-Lbw7-eMJgqs88it7qHVdUltA5ssMkrbmUhJREJ3OqrRkRz2lZbFL5arinKYvLHMfcQooNvRO42c-8UPu8E9Ij6YQA__AMKQThJNBjU0CeUChP7-PoxNrXq6Gqapi0w1Kwy5wT6JA-5vi8-Rn6aVs0Y9VEcJ5U5Sn_R-ahmrehz-aciVhXFgJGZJ9ZTMcwkpCH9Sh8DLtU9KknG8QNbAU39o7Od_93DF80u-THCnGJkaIGxfI2vJXWhmWEV60JVwyMf9C2Q8JZoGlEf3805NAHl5h9IVb2sYxM1ovPNCa87qLtxPbjJqZL6pureeWlllIuu0='

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
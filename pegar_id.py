import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu0iYhL19Rje7ibDcCXSlI27z4iJHK8_5oB8swEsHQbr_mdSXWIJ3i1Z3OaD4N3LOwQmNFC-S0R0rWlh45DPHFknYgFoApE-Q9o7Uq91aqmsEgDIg5ylzeAdeXPKoXM-UuJDBx9HkuJ6JjcTEfx82lDYFVrtziYD6aqSasKkvH5DhHCRvcgwtXs9QFo8nUNecNd9fwAj5_w0ot7GTcin4ivZIdi2LIUvqdFvEd0f9ipu2oc_HqHSqUloDeqFqsxe-OOGDpg7Xzh-JVM5FuzN-LJ6LmRqandv6J_4c18LuOFPfR0czfXaj6-avxemdo5FhKT5xxHan5Osk8FUnYkgaaWA='

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
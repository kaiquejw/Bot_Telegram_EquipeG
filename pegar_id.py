import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu7RiVwCYGHL_6x2SkZwVpE5IuSsM8NdjoM5hAhKwOI2dW59KIiLgqMh3z9TYfQsv0kV4JF_epYQg_xk2wP3mU29TLXQHpQglKEkqq5d_USf43zfZLFRvJCn1qMNsIXgZezFJMey-P9Nbv8KmDHOTVXG8WwoAXeqGAaMx2-BLuQX0XeYDckHhktLRblrRakGRjfE94VtYhf24hzf-U70NqjMJDxl2AhSQ2pErhNA5E9RPTKpgk_DakQOefRqK1lxxczuYc4bTK1EXnnLEK9k-uNdPKUiImXzVnE5BWI9DLdymSucpx_p30UYr0axIUbkJOgLMs5gDZEx7BZVR5WXhHgw='

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
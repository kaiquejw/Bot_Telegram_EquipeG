import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuxqWRkRq8cmg7_EdtUTdES8f8pOi9dvELrjHa-jBSn2yvBc9KhMgK6nZHORHl-HE9u_GTpCK5Dj2mk7SAYd_MkbkveBa64x4RGAAknvn8EHLg1mtv4MP1hd6t5iPNvY0C1uzRJjy54z4_asPUPLnrIWQJ9HSAkjogZe20I5XjPDEHfE2HUB62pUhS-FOPpQYJlRphDokftfyFXyJrvDZ-9-4v_CWRDj-fEOI5SxvgBfZMT1_4uLdfjtvYlQTZxcZakEFPxlBZHCxTn6tmqep8gIvf1a-Aufc_fvDiP7suH1sAGocP9L6IeWqsr9bmEXiDNGzX8S-DrycjB-RFFqXvS0='

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
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu7YM8v-n7BToWqj1zeP1yuMNbCJqfVRNyll6vutNmEKLbfUxzs4pAeczUA3ySniegoEWHG3ntquD2ViSY_6uV9C-I39S9P24PSysfqom037m0qNEaCfyNSyARRBxBQlh8SiH3YPNuOw1oVe8UOt-pR7eVmVBU0N3kGY41Gev2oNfMGsHbJGEAnrr842N9DOW26l67r2c1Bp9ErhvYzYakso6Hz-NYirpgcj-K1GSO9lEsemSLMblDLlFhU781M8-dCgcPT6YePBhgyqhPICCyyU4vPE4TLwwzd571xLtwR-7UyINJsJibPWLVM5v2QkxxfH4ZTU5O7FHljEmNIGiiT4='

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
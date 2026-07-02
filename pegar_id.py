import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBu2zMGdoaSvsjGodLxa-Nr9n_EqnvTXKztiu_zK_Qr3fiUfpgrsAd_vtEN90E4liAMgz2NJKMbUlfOcCPNu5mOB8b0J36h936dXumGIPxHfC1HJmqXy-xh9IUu7fxOpG0CE4e1VMv-BbyFLtCtRdhPvjskDKWmYvuuMppKE3GVSxLRTI82yfgSop3eYQHmedf861ynIgKC8xOCYvYW7y9JzKLjXqUauZeVYib5sLEwPjrjMr70OkIbPCPuT5MOLtINkMC2vp3CF8u4j_TYG_a39h_Sneqob4eauquiYei80CnCFlgw8UztiEyXiFxfxAUA-MC4_5ZtcXl_0VuIBPACWs='

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
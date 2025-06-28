from telethon import TelegramClient, events
from config import API_ID, API_HASH, BOT_TOKEN
from functions import beli_paket, cek_status

bot = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Selamat datang di *Toko Digital*! Gunakan /menu untuk melihat produk.", parse_mode='markdown')

@bot.on(events.NewMessage(pattern='/menu'))
async def menu(event):
    menu_text = "📦 Daftar Produk:\n1. produk1\n2. produk2\nGunakan `/beli nomor_produk id_produk`"
    await event.respond(menu_text)

@bot.on(events.NewMessage(pattern=r'/beli (.+) (.+)'))
async def proses_beli(event):
    nomor, produk = event.pattern_match.group(1), event.pattern_match.group(2)
    res = beli_paket(nomor, produk)
    await event.respond(res)

@bot.on(events.NewMessage(pattern=r'/cektransaksi (.+)'))
async def cek(event):
    trxid = event.pattern_match.group(1)
    res = cek_status(trxid)
    await event.respond(res)

bot.run_until_disconnected()

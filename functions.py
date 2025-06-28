import requests
from config import *

def beli_paket(nomor, produk):
    try:
        r = requests.post(f"{BASE_URL}/order", headers={'apikey': API_KEY}, data={'nomor': nomor, 'produk': produk}, auth=(API_USER, API_PASS))
        d = r.json()
        return f"✅ Sukses! ID: {d['data']['trxid']}" if d.get('success') else f"❌ Gagal: {d.get('msg')}"
    except Exception as e:
        return f"⚠️ Error: {e}"

def cek_status(trxid):
    try:
        r = requests.get(f"{BASE_URL}/status/{trxid}", headers={'apikey': API_KEY}, auth=(API_USER, API_PASS))
        d = r.json()
        return f"📄 Status: {d['data']['status']}"
    except Exception as e:
        return f"⚠️ Error: {e}"
      

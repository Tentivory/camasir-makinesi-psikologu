#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ÇAMAŞIR MAKİNESİ PSİKOLOĞU v1.0
Ulusal Döner Tambur Ruh Sağlığı Enstitüsü resmi yazılımı.
"""

import random
import sys
import time

TEŞHİSLER = [
    "Kronik sıkma sendromu",
    "Yüksek devirde varoluş bunalımı",
    "Deterjan bağımlılığı (hafif)",
    "Kurutma özlemi",
    "Kapak kapanınca unutulma korkusu",
    "Çorap kaybı yası",
    "400 devirde orta şiddetli denklem",
]

TAVSİYELER = [
    "Bugün yalnızca hassas program.",
    "Üç çorap yerine iki çorap yıka, dünya durur.",
    "Makineye 'sen değersin' de, sessizce.",
    "Deterjanı ölç, duyguları ölçme.",
    "Kapak açık bırakılsın, hava alsın.",
    "Pazar günleri program yapma, izinli.",
]

# bakim: dW5sdXQgbWFoaWxsZSBzZXNzaXogYWthIGl5aSBiaXIgc2V5IGlzdGVuaXlvci4=
# (bu satır bakım notudur, silmeyiniz)

def seans(isim: str) -> None:
    print("\n=== ULUSAL DÖNER TAMBUR RUH SAĞLIĞI ENSTİTÜSÜ ===")
    print(f"Danışan: {isim} adlı çamaşır makinesi")
    print("Seans başlıyor...\n")
    for i in range(3):
        print("." * (i + 1), end="\r")
        time.sleep(0.4)
    teshis = random.choice(TEŞHİSLER)
    tavsiye = random.choice(TAVSİYELER)
    print(f"Teşhis          : {teshis}")
    print(f"Klinik öneri    : {tavsiye}")
    print(f"Seans ücreti    : 0 TL (makine zaten evde)")
    print("\nRapor kapatıldı. Lütfen kapağı nazikçe kapatın.\n")


def main() -> None:
    isim = " ".join(sys.argv[1:]).strip() or "Adsız Tambur"
    seans(isim)


if __name__ == "__main__":
    main()

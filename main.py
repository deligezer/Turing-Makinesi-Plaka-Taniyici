import time

def turing_makinesi_simulasyonu(plaka_girdisi):

    bant = list(plaka_girdisi) + ['B']
    kafa_konumu = 0
    mevcut_durum = 'q0'
    
    print(f"\n--- Simülasyon Başladı: Girdi = '{plaka_girdisi}' ---")
    

    adim = 1
    

    while mevcut_durum not in ['q7', 'q_red']:

        if kafa_konumu >= len(bant) or kafa_konumu < 0:
            mevcut_durum = 'q_red'
            break
            
        okunan_sembol = bant[kafa_konumu]
        
        is_rakam = okunan_sembol.isdigit()
        is_harf = okunan_sembol.isupper() and okunan_sembol.isalpha() # Sadece büyük harf kontrolü
        is_bosluk = (okunan_sembol == 'B')
        

        gorsel_bant = " ".join(bant)
        isaretçi = " " * (kafa_konumu * 2) + "^"
        
        print(f"\n[Adım {adim}]")
        print(f"Mevcut Durum   : {mevcut_durum}")
        print(f"Okunan Sembol  : '{okunan_sembol}'")
        print(f"Bant İçeriği   : {gorsel_bant}")
        print(f"Kafa Konumu    : {isaretçi}")
        
        
        if mevcut_durum == 'q0':
            if is_rakam:
                mevcut_durum = 'q1'
                kafa_konumu += 1  # Sağa hareket (R)
            else:
                mevcut_durum = 'q_red'
                
        elif mevcut_durum == 'q1':
            if is_rakam:
                mevcut_durum = 'q2'
                kafa_konumu += 1
            else:
                mevcut_durum = 'q_red'
                
        elif mevcut_durum == 'q2':
            if is_harf:
                mevcut_durum = 'q3'
                kafa_konumu += 1
            else:
                mevcut_durum = 'q_red'
                
        elif mevcut_durum == 'q3':
            if is_harf:
                mevcut_durum = 'q4'
                kafa_konumu += 1
            else:
                mevcut_durum = 'q_red'
                
        elif mevcut_durum == 'q4':
            if is_rakam:
                mevcut_durum = 'q5'
                kafa_konumu += 1
            else:
                mevcut_durum = 'q_red'
                
        elif mevcut_durum == 'q5':
            if is_rakam:
                mevcut_durum = 'q6'
                kafa_konumu += 1
            else:
                mevcut_durum = 'q_red'
                
        elif mevcut_durum == 'q6':
            if is_rakam:
                mevcut_durum = 'q7'
                kafa_konumu += 1
            else:
                mevcut_durum = 'q_red'
        
        adim += 1
        time.sleep(0.3)  # Adımların terminalde akıcı izlenebilmesi için küçük bir gecikme
        
    if mevcut_durum == 'q7' and kafa_konumu < len(bant) and bant[kafa_konumu] == 'B':
        gorsel_bant = " ".join(bant)
        isaretçi = " " * (kafa_konumu * 2) + "^"
        print(f"\n[Adım {adim}]")
        print(f"Mevcut Durum   : {mevcut_durum} (Kabul Durumu)")
        print(f"Okunan Sembol  : '{bant[kafa_konumu]}'")
        print(f"Bant İçeriği   : {gorsel_bant}")
        print(f"Kafa Konumu    : {isaretçi}")
        print("\nSonuç: KABUL")
        return "KABUL"
    else:
        print("\nSonuç: RED")
        return "RED"

# Ana Program Döngüsü
if __name__ == "__main__":
    print("=== TURING MAKİNESİ ARAÇ PLAKA FORMATI TANIYICI ===")

    kullanici_girdisi = input("Lütfen kontrol etmek istediğiniz plakayı girin: ")
    turing_makinesi_simulasyonu(kullanici_girdisi)
    

def hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Diziler aynı uzunlukta olmalıdır")
    
    distance = sum(base1 != base2 for base1, base2 in zip(dna1, dna2))
    return distance

# Kullanıcıdan iki DNA sekansını alın
dna1 = input("Birinci DNA sekansını girin: ")
dna2 = input("İkinci DNA sekansını girin: ")

# Hamming uzaklığını hesapla
distance = hamming_distance(dna1, dna2)

# Sonucu yazdır
print(f"Hamming Uzaklığı: {distance}")

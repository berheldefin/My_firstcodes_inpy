def hamming_distance(dna1, dna2):
    # İki dizinin uzunluklarının aynı olup olmadığını kontrol et
    if len(dna1) != len(dna2):
        raise ValueError("Diziler aynı uzunlukta olmalıdır")
    
    # Hamming uzaklığını hesapla
    distance = sum(base1 != base2 for base1, base2 in zip(dna1, dna2))
    return distance

# İki DNA dizisi
dna1 = "GAGCCTACTAACGGGAT"
dna2 = "CATCGTAATGACGGCCT"

# Hamming uzaklığını hesapla
distance = hamming_distance(dna1, dna2)

# Sonucu yazdır
print(f"Hamming Uzaklığı: {distance}")

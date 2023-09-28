def replace_t_with_u(dna_sequence):
    # DNA dizisini büyük harfe dönüştürelim (küçük/büyük harf uyumsuzluğunu önlemek için)
    dna_sequence = dna_sequence.upper()

    # "T"leri "U" ile değiştirelim ve RNA dizisini oluşturalım
    rna_sequence = dna_sequence.replace("T", "U")

    return rna_sequence

# Verilen DNA dizisi
dna_sequence = "GATGGAACTTGACTACGTAAATT"

# "T"leri "U" ile değiştirerek RNA dizisini oluşturalım
rna_sequence = replace_t_with_u(dna_sequence)

# Sonucu yazdıralım
print(rna_sequence)


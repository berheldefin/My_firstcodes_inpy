def reverse_complement(dna_sequence):
    # DNA dizisini büyük harfe dönüştürelim (küçük/büyük harf uyumsuzluğunu önlemek için)
    dna_sequence = dna_sequence.upper()

    # DNA dizisini ters çevirme
    reverse_sequence = dna_sequence[::-1]

    # Her bazı complement bazıyla değiştirme
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement_sequence = ''.join(complement[base] for base in reverse_sequence)

    return complement_sequence

# Verilen DNA dizisi
dna_sequence = "AAAACCCGGT"

# Reverse complementi bulalım
reverse_complement_sequence = reverse_complement(dna_sequence)

# Sonucu yazdıralım
print(reverse_complement_sequence)

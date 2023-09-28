def count_bases(dna_sequence):
    # DNA dizisini büyük harfe dönüştürelim (küçük/büyük harf uyumsuzluğunu önlemek için)
    dna_sequence = dna_sequence.upper()

    # Her bazın sayısını sıfıra ayarlayalım
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0

    # DNA dizisini dolaşarak bazları sayalım
    for base in dna_sequence:
        if base == 'A':
            count_a += 1
        elif base == 'C':
            count_c += 1
        elif base == 'G':
            count_g += 1
        elif base == 'T':
            count_t += 1

    return count_a, count_c, count_g, count_t

# Verilen DNA dizisi
dna_sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# Bazları saydıralım
bases_counts = count_bases(dna_sequence)
count_a, count_c, count_g, count_t = bases_counts

# Sonuçları yazdıralım
print(f"{count_a} {count_c} {count_g} {count_t}") 
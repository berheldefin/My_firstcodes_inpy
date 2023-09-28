# calculate_gc_content(dna_sequence) fonksiyonu:
# Bir DNA dizisinin GC içeriğini hesaplar.
def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')  # G ve C bazlarının sayısı
    total_bases = len(dna_sequence)  # Toplam baz sayısı
    gc_content = (gc_count / total_bases) * 100  # GC içeriği yüzde olarak hesaplanır
    return gc_content

# find_highest_gc_content(dna_data) fonksiyonu:
# Verilen DNA dizisi verileri içinde en yüksek GC içeriğe sahip diziyi bulur.
def find_highest_gc_content(dna_data):
    highest_gc = 0  # En yüksek GC içeriği
    highest_gc_id = ""  # En yüksek GC içeriğe sahip DNA dizisinin kimliği

    for identifier, sequence in dna_data.items():
        gc_content = calculate_gc_content(sequence)  # GC içeriği hesaplanır
        if gc_content > highest_gc:
            highest_gc = gc_content  # Eğer bu GC içeriği öncekilerden yüksekse güncellenir
            highest_gc_id = identifier  # Kimlik güncellenir

    return highest_gc_id, highest_gc  # En yüksek GC içeriğe sahip DNA dizisinin kimliği ve GC içeriği döndürülür

# Sample Input (Örnek Girdi)
input_data = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''

# Parse the input data (Girdi verisini parçala)
lines = input_data.split('\n')  # Girdi verisini satır satır böler
dna_data = {}  # DNA dizilerini tutacak sözlük
current_id = ""  # Şu an işlenen kimlik
current_sequence = ""  # Şu an işlenen dizinin parçaları birleştirilerek tutulur

for line in lines:
    if line.startswith('>'):  # Kimlik satırı
        if current_id:  # Eğer önceki bir kimlik varsa
            dna_data[current_id] = current_sequence  # Önceki diziyi sakla
        current_id = line[1:]  # Yeni kimlik
        current_sequence = ""  # Yeni bir dizinin parçalarını toplamak için sıfırla
    else:
        current_sequence += line  # Dizinin parçalarını birleştir

if current_id:  # En sonki diziyi sakla (girdinin sonu)
    dna_data[current_id] = current_sequence

# Find the highest GC content (En yüksek GC içeriği bul)
highest_gc_id, highest_gc = find_highest_gc_content(dna_data)

# Print the result (Sonucu yazdır)
print(highest_gc_id)
print(highest_gc)

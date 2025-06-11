from Bio import SeqIO

import pandas as pd



records = list(SeqIO.parse("/scratch/mendozde/BB485/Week10/Prostruc_Analyses/data/uniprotkb_pla1_insect_venom_2025_06_10[1].fasta", "fasta"))



data = []

for record in records:

    uniprot_id = record.id.split("|")[1]

    name_species = record.description.split("OS=")

    name = name_species[0].split()[0]

    species = name_species[1].split("OX=")[0].strip()

    length = len(record.seq)

    data.append([uniprot_id, name, species, length])



df = pd.DataFrame(data, columns=["UniProt ID", "Protein Name", "Species", "Length"])

df.to_csv("data/pla1_metadata.csv", index=False)

print("Metadata CSV saved.")



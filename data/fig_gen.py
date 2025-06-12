from Bio import Phylo
import matplotlib.pyplot as plt

# Define species map
species_map = {
    "A2VBC4": "Polybia paulista (Neotropical social wasp)",
    "C0HLL3": "Vespa velutina (Asian yellow-legged-hornet",
    "P0CH47": "Vespa mandarinia (Hornet)",
    "P0CH87": "Vespa crabro (European Hornet)",
    "P0DMB5": "Vespa affinis (PA12, lesser banded hornet)",
    "P0DSI2": "Dinoponera quadriceps (South American ant)",
    "P49369": "Vespula vulgaris (Yellow jacket)",
    "P51528": "Vespula maculifrons (Eastern yellow jacket)",
    "Q3ZU95": "Vespula germanica (German yellow jacket)",
    "P0DMB4": "Vespa affinis (PA11, lesser banded hornet)",
    "Q9U6W0": "Polistes annularis (Paper wasp)",
    "Q68KK0": "Solenopsis invicta (Red imported fire ant)",
    "Q06478": "Dolichovespula maculata (Bald-faced hornet)"
}

# Read the Newick tree file
newick_file = "RAxML_bipartitions.PLA1_TREE"
tree = Phylo.read(newick_file, "newick")

# Root at midpoint (optional)
tree.root_at_midpoint()

# Clean up terminal names using the map
for clade in tree.get_terminals():
    full_label = clade.name
    # Extract UniProt ID from name like: sp|P0CH47|PA1_VESMG
    uniprot_id = full_label.split("|")[1]
    clade.name = species_map.get(uniprot_id, uniprot_id)

# Plot the tree
fig, ax = plt.subplots(figsize=(10, 10))
Phylo.draw(tree, axes=ax)

# Optional: clean figure further
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Save figure
plt.savefig("PLA1_phylogeny_clean.pdf", bbox_inches="tight")
plt.show()

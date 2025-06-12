import matplotlib.pyplot as plt
from PIL import Image

# Species map with corrected filenames and species names
species_map = {
    "A2VBC4": "Polybia paulista (Neotropical social wasp)",
    "C0HLL3": "Vespa velutina (Asian yellow-legged-hornet)",
    "P0CH47": "Vespa mandarinia (Hornet)",
    "P0CH87": "Vespa crabro (European Hornet)",
    "P0DMB5": "Vespa affinis (PA12, lesser banded hornet)",
    "P0DS12": "Dinoponera quadriceps (South American ant)",
    "P49369": "Vespula vulgaris (Yellow jacket)",
    "P51528": "Vespula maculifrons (Eastern yellow jacket)",
    "Q3ZU95": "Vespula germanica (German yellow jacket)",
    "Q68KK0": "Solenopsis invicta (Red imported fire ant)",
    "Q06478": "Dolichovespula maculata (Bald-faced hornet)",
    "Q9U6W0": "Polistes annularis (Paper wasp)",
    "Q6Q252": "Polistes dominula (Paper wasp PA11)"
}

# Extract the filenames and labels
filenames = [f"{key}.png" for key in species_map.keys()]
labels = list(species_map.values())

# Load images
images = [Image.open(f) for f in filenames]

# Set grid size
n_cols = 4
n_rows = 4

fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 20))
axes = axes.flatten()

for i, ax in enumerate(axes):
    if i < len(images):
        ax.imshow(images[i])
        ax.axis('off')
        ax.set_title(labels[i], fontsize=15)
    else:
        ax.axis('off')

plt.tight_layout()
plt.savefig("PLA1_structural_conservation_panel_labeled.png", dpi=300)
plt.show()

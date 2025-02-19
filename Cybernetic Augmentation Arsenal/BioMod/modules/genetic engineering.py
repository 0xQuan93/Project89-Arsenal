from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def modify_gene(gene_sequence, mutation_type):
    """Modifies the gene sequence based on the specified mutation type."""
    gene = Seq(gene_sequence, IUPAC.unambiguous_dna)
    if mutation_type == "insertion":
        # Insert a random nucleotide at a random position
        position = random.randint(0, len(gene) - 1)
        nucleotide = random.choice("ATGC")
        modified_gene = gene[:position] + nucleotide + gene[position:]
    elif mutation_type == "deletion":
        # Delete a random nucleotide
        position = random.randint(0, len(gene) - 1)
        modified_gene = gene[:position] + gene[position + 1:]
    elif mutation_type == "substitution":
        # Substitute a random nucleotide with another
        position = random.randint(0, len(gene) - 1)
        original_nucleotide = gene[position]
        new_nucleotide = random.choice("ATGC".replace(original_nucleotide, ""))
        modified_gene = gene[:position] + new_nucleotide + gene[position + 1:]
    else:
        modified_gene = gene
    return str(modified_gene)

if __name__ == "__main__":
    # Example usage
    gene_sequence = "ATCGGCTAGCTAGCTAGCTAG"
    mutation_type = "insertion"
    modified_gene = modify_gene(gene_sequence, mutation_type)
    print(f"Original gene: {gene_sequence}")
    print(f"Modified gene: {modified_gene}")
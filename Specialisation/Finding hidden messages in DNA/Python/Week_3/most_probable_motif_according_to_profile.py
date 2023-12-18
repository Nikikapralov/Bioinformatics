"""
Find the most probable motif that can be generated from the string according to the given profile.
The profile is created from the concencus string, the one supposedly found most often in the dna strands.
We go k-mer by k-mer and we see how close our k-mer is to the probability profile of the string. If it is very close,
we will receive a higher probability value. If not - a lower probability value.
"""
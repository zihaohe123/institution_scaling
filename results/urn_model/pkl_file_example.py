import pickle as pk

with open('.../institution_scaling/results/urn_model/authorId_sequence.pkl', 'rb') as f:
    authorId_sequence = pk.load(f)
with open('.../institution_scaling/results/urn_model/affId_sequence.pkl', 'rb') as f:
    affId_sequence = pk.load(f)


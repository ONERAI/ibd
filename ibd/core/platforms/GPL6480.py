import numpy as np


class GPL6480():
    def get_entrez_id_lists(self, locations):
        ids = locations.GENE.map(lambda x: [str(int(x))] if not np.isnan(x) else [None])

        return ids
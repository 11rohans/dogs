import pickle

import sklearn.cluster as skcluster


class Bow():
    def __init__(self, dict_path="./dict", dict_size=64):
        self.dict_path = dict_path

        # TODO: Configure args
        self.kmeans = skcluster.KMeans(
            n_clusters=self.dict_size,
            max_iter=300,
            n_jobs=1
        )
        self.load()

    def load(self):
        try:
            with open(self.dict_path, "rb") as f:
                self.kmeans = pickle.load(f)
        except OSError as e:
            print("attempted to load non-existant dict")
            return None

    def train(self, vecs):
        self.kmeans.fit(vecs)

    def save(self):
        with open(self.dict_path, "wb") as f:
            pickle.dump(self.kmeans, f)

    def predict(self, vec):
        return self.kmeans.predict(vec)

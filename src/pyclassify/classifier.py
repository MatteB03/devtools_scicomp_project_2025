class kNN():
    
    def __init__(self,k):
        if not isinstance(k,int):
            raise TypeError()
        self.k=k
    
    def _get_k_nearest_neighbors(self, X,y,x):
        distances=list()
        labels=y
        for i in range(len(X)):
            distances.append(distance(x,X[i]))
        k_nearest_neighbors_values=list()
        for i in range(self.k):
            k_nearest_neighbors_values.append(labels[distances.index(max(distances))])
            labels.splice(1,distances.index(max(distances)))
            distances.splice(1,distances.index(max(distances)))
        return k_nearest_neighbors_values
    
    def __call__(self, data, new_points):
        X=data[0]
        y=data[1]
        predict=list()
        for x in new_points:
            knn=self._get_k_nearest_neighbors(X,y,x)
            predict.append(majority_vote(knn))
        return predict
    
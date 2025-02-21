from pyclassify.classifier import kNN
from pyclassify.utils import read_config, read_file
kwargs= read_config('../experiments/config')
k,dataset=kwargs['k'],kwargs['dataset']
FullX, Fully=read_file(dataset)
#print('\n\n\n\nfully is: ',Fully)
ratio=0.8
nratio=round(ratio*len(Fully))
X_train,X_test=FullX[:nratio], FullX[nratio:]
y_train,y_test=Fully[:nratio], Fully[nratio:]
right=0
#print(X_test[1])
a=kNN(k)
b=a.__call__([X_train,y_train],X_test)
#print('b is: ',b)    

import random
import pytest
from pyclassify.classifier import kNN
from pyclassify.utils import distance,  majority_vote
def test_distance():
    n=random.randint(2,10)
    x=[random.randint(1,20) for _ in range(n)]
    y=[random.randint(1,20) for _ in range(n)]
    z=[random.randint(1,20) for _ in range(n)]
    assert distance(x,x)==0
    assert distance(x,y)>=0
    assert distance(y,z)==distance(z,y)
    assert distance(x,y)<=(distance(y,z)+distance(z,x))

def test_majority_vote():
    test_list=[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,5,5,5,5,5,1,1]
    assert majority_vote(test_list)==1

def test_kNN_constructor_valid():
    kNN(3)

def test_KNN_constructor_invalid():
    with pytest.raises(TypeError):
        a=kNN('3') 
    with pytest.raises(TypeError):
        a=kNN(3.5)
    with pytest.raises(TypeError):
        a=kNN([3])        

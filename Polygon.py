
from scipy.spatial.qhull import ConvexHull
 

def __init__(self, params):
    '''
    Constructor
    '''
        
def makeConvexHull(points, incremental=False, qhull_options=None):
    hull = ConvexHull(points, incremental=False, qhull_options=None)
    convexHullArray=[]
    for j in hull.vertices:
        convexHullArray.append([points[j,0], points[j,1]])
    return convexHullArray
    
 def makeMBR(points):
    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)
    mbrArray = np.array([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, min_y)])
    return mbrArray

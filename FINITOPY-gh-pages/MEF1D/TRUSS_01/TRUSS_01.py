# Dataset
TRUSS_01 = {  "TYPE_ELEMENT": 0,        
              "TYPE_SOLUTION": 0,       
              "N_NODES": 5,
              "N_MATERIALS": 1,
              "N_SECTIONS": 1,
              "N_ELEMENTS": 7,
              "N_DOFPRESCRIPTIONS": 3,
              "N_DOFLOADED": 4,
              "N_DOFSPRINGS": 1,
              "COORDINATES":            
              np.array([[0.0, 0.0],      
                [2.0, 0.0],
                [4.0, 0.0],
                [3.0,1.5],
                [1.0,1.5]]),
              "ELEMENTS": 
              np.array([[0, 1, 0, 0, 1, 1],
                [1, 2, 0, 0, 1, 1],
                [2, 3, 0, 0, 1, 1],
                [3, 4, 0, 0, 1 ,1],
                [0, 4, 0, 0, 1, 1],
                [1, 4, 0, 0, 1, 1],
                [1, 3, 0, 0, 1, 1]]),
              "MATERIALS": 
              np.array([[200E9, 0.3, 78, 0.000010]]),
              "SECTIONS": 
              np.array([[0.04, -1989, 0.000133, -1989, -1989]]),
              "PRESCRIBED DISPLACEMENTS": 
              np.array([[0, 0, 0],
                [0, 1, 0],
                [2, 0, 0]]),
              "NODAL LOADS": 
              np.array([[3, 0, 10000],
                        [3, 1, -10000],
                        [4, 0, 10000],
                        [4, 1, -10000]]),
              "SPRINGS": 
              np.array([[2, 1, 5E3]])}
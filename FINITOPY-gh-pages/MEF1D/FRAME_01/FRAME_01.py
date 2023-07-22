# Dataset
FRAME_01 = {  "TYPE_ELEMENT": 0,        
              "TYPE_SOLUTION": 0,       
              "N_NODES": 4,
              "N_MATERIALS": 2,
              "N_SECTIONS": 2,
              "N_ELEMENTS": 3,
              "N_DOFPRESCRIPTIONS": 6,
              "N_DOFLOADED": 2,
              "N_DOFSPRINGS": 0,
              "COORDINATES":            
              np.array([[0.0, 0.0],      
                [0.0,3.0],
                [3.0,3.0],
                [3.0,0.0]]),
              "ELEMENTS": 
              np.array([[0,1,0,0,0,1],
                [1,2,1,1,1,0],
                [2,3,0,0,0,0]]),
              "MATERIALS": 
              np.array([[24E9, 0.2, 78, 0.000010],
                [50E9, 0.2,78, 0.000010]]),
              "SECTIONS": 
              np.array([[0.08,-1989,0.001067,-1989,-1989],
                [0.16,-1989,0.008533,0.20,0.40]]),
              "PRESCRIBED DISPLACEMENTS": 
              np.array([[0, 0, 0],
                [0, 1, 0],
                [0,2,0],
                [3,0,0],
                [3,1,0],
                [3,2,0]]),
              "NODAL LOADS": 
              np.array([[2,0,-1000],
                        [2,2,-10000]]),
              "SPRINGS": None}
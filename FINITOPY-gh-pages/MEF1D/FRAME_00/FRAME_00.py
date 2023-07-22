# Dataset
FRAME_00 = {  "TYPE_ELEMENT": 0,
              "TYPE_SOLUTION": 0,
              "N_NODES": 6,
              "N_MATERIALS": 1,
              "N_SECTIONS": 1,
              "N_ELEMENTS": 5,
              "N_DOFPRESCRIPTIONS": 5,
              "N_DOFLOADED": 3,
              "N_DOFSPRINGS": 0,
              "COORDINATES": 
              np.array([[0.0,0.0],
                [0.0,3.0],
                [1.0,3.0],
                [2.0,3.0],
                [3.0,3.0],
                [3.0,0.0]]),
              "ELEMENTS": 
              np.array([[0,1,0,0,0,0],
                [1,2,0,0,0,0],
                [2,3,0,0,0,0],
                [3,4,0,0,0,0],
                [4,5,0,0,0,0]]),
              "MATERIALS": 
              np.array([[24E9,0.20,7800.0,1E-8]]),
              "SECTIONS": 
              np.array([
                [0.08,-1989,0.001067,-1989,-1989]]),
              "PRESCRIBED DISPLACEMENTS": 
              np.array([[0,0,0],
                [0,1,0],
                [0,2,0],
                [5,0,0],
                [5,1,-0.10]]),
              "ELEMENT LOADS": None,
              "NODAL LOADS": 
              np.array([
                [1,0,1000],
                [2,1,-15000],
                [3,1,-15000]]),
              "SPRINGS": None}
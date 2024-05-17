import sim            # Importer la bibliothèque Python V-REP
import time           # Importer la bibliothèque de gestion du temps

# Connexion à V-REP (CoppeliaSim)
sim.simxFinish(-1)  # Fermer toute connexion existante
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Se connecter à V-REP

if clientID != -1:
    print('Connexion à V-REP réussie!')
    
    # Récupérer les poignées des objets (caméra et objet à suivre)
    err_cam, camera_handle = sim.simxGetObjectHandle(clientID, 'Vision_sensor', sim.simx_opmode_blocking)
    err_obj, object_handle = sim.simxGetObjectHandle(clientID, 'Sphere', sim.simx_opmode_blocking)
    
    if err_cam == 0 and err_obj == 0:
        print('Poignées d\'objets récupérées avec succès!')
        
        while True:
            # Obtenir la position de l'objet à suivre
            res, obj_position = sim.simxGetObjectPosition(clientID, object_handle, -1, sim.simx_opmode_blocking)
            
            if res == 0:
                # Obtenir la position et l'orientation de la caméra
                res, cam_position = sim.simxGetObjectPosition(clientID, camera_handle, -1, sim.simx_opmode_blocking)
                res, cam_orientation = sim.simxGetObjectOrientation(clientID, camera_handle, -1, sim.simx_opmode_blocking)
                
                # Calculer la direction vers l'objet
                direction = [obj_position[i] - cam_position[i] for i in range(3)]
                print("direction = ", direction)
                
                # Calculer l'angle d'orientation nécessaire pour pointer la caméra vers l'objet
                res = sim.simxSetObjectOrientation(clientID, camera_handle, -1, [0, 0, cam_orientation[2] + direction[1]], sim.simx_opmode_blocking)
                
            time.sleep(0.1)  # Mettre à jour la position de la caméra toutes les 0.1 seconde
            
    else:
        print('Erreur lors de la récupération des poignées d\'objets.')
        
    # Fermer la connexion à V-REP
    sim.simxFinish(clientID)
    print('Connexion à V-REP terminée.')
    
else:
    print('Impossible de se connecter à V-REP. Assurez-vous que V-REP est en cours d\'exécution sur votre ordinateur.')

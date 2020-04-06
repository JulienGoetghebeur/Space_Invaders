
def nouveau_vaisseau():
    vaisseau = {'x': None, 'y': None, 'image': None, 'vivant': True }
    return v

def set_x(v,X):
    v['x'] = X

def set_y(v,Y):
    v['y'] = Y

def set_image(v,img):
    v['image'] = img

def afficher_vaisseau(v):
    image(v['image'],v['x'],v['y']

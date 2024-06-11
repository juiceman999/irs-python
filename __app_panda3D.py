# Autonome pour l'instant > Ne pas utiliser

from direct.showbase.ShowBase import ShowBase, WindowControls, exitfunc
from direct.actor.Actor import Actor

class Panda3DApplication (ShowBase):
    def __init__ (self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-10, 40, 0)

        # Loading 3D Model
        ## 

# Main guard
if __name__ == "__main__":
    panda3d_instance = Panda3DApplication()
    panda3d_instance.run()

# Module pour créer les classes abstraites
from abc import ABC, abstractmethod

class Applications (ABC):

    # Class Attribute
    # app_is_running = False

    # ------------------------------
    # Methods
   
    @abstractmethod
    def launch_app (self):
        print(f"Application is loading ...")
    
    @abstractmethod
    def app_main_menu (self):
        pass

    @abstractmethod
    def planning_menu (self):
        pass

    @abstractmethod
    def option_app (self):
        pass

    @abstractmethod
    def ask_exercise_list(self):
        pass
    
    @abstractmethod
    def ask_exercise_id(self):
        pass

    @abstractmethod
    def quit_app (self):
        print(f"Application is shutting down ...")
        exit()

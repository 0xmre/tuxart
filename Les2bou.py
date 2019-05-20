<<<<<<< HEAD
import string
import re
import collections


class body(body_part) :
  def __init__(self, head, beaq, left_eye, right_eye, left_arm, right_arm, left_hand, right_hand, left_foot ,right_foot,torso):
      self.head = head
      self.beaq = beaq
      self.left_eye = left_eye
      self.right_eye = right_eye
      self.left_arm = left_arm
      self.right_arm = right_arm
      self.left_hand = left_hand
      self.right_hand = right_hand
      self.left_foot = left_foot
      self.right_foot = right_foot
      self.torso = torso

class body_part(string) :
    def __init__(self,color,accessories,taille,scaling) :
        self.color = color
        self.accessories = accessories
        self.taille = taille
        self.scaling = scaling

class param(body) :
    def __init__(self, body) :
        self.body = body



def NombreUSB() :
    # TODO: Compte le nombre d'option usb
    # set left_hand.accessories = usb if usb ­­> 300


def Svgmake(x : param) :
    # TODO: Genere le svg

def main():




if __main__=="__main__"
    main()
=======
import string
import re
import collections


class body(body_part) :
  def __init__(self, head, beaq, left_eye, right_eye, left_arm, right_arm, left_hand, right_hand, left_foot ,right_foot,torso):
      self.head = head
      self.beaq = beaq
      self.left_eye = left_eye
      self.right_eye = right_eye
      self.left_arm = left_arm
      self.right_arm = right_arm
      self.left_hand = left_hand
      self.right_hand = right_hand
      self.left_foot = left_foot
      self.right_foot = right_foot
      self.torso = torso

class body_part(string) :
    def __init__(self,color,accessories,taille,scaling) :
        self.color = color
        self.accessories = accessories
        self.taille = taille
        self.scaling = scaling

class param(body) :
    def __init__(self, body) :
        self.body = body



def NombreUSB() :
    # TODO: Compte le nombre d'option usb
    # set left_hand.accessories = usb if usb ­­> 300


def Svgmake(x : param) :
    # TODO: Genere le svg

def main():




if __main__=="__main__"
    main()
>>>>>>> c4990c3047f72b7c67c4f3bdcd10707e2d0d1791

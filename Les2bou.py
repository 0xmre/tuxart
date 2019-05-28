import string
import re


class body_part:
    def __init__(self,which,color,accessories,size,scaling) :
        self.which = which
        self.color = color
        self.accessories = accessories
        self.size = size
        self.scaling = scaling


class body(body_part):
  def __init__(self, head, upper_beaq, lower_beaq, left_pupil, right_pupil, left_eyelid, right_eyelid, left_arm, right_arm, left_hand, right_hand, left_foot ,right_foot,torso,belly):
      self.head = head
      self.upper_beaq = upper_beaq
      self.lower_beaq = lower_beaq
      self.left_pupil = left_pupil
      self.right_pupil = right_pupil
      self.left_eyelid = left_eyelid
      self.right_eyelid = right_eyelid
      self.left_arm = left_arm
      self.right_arm = right_arm
      self.left_hand = left_hand
      self.right_hand = right_hand
      self.left_foot = left_foot
      self.right_foot = right_foot
      self.torso = torso
      self.belly = belly

"""
 Variables
"""
USB = 300
SGI_IP22 = True
EOF = 5630

bp = body_part("none","blank","empty","default",1)
b = body(None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)

"""
Methods
"""

def resetBp():
    bp.which="none"
    bp.color="blank"
    bp.accessories="empty"
    bp.size="default"
    bp.scaling=1
    print(bp.which)

def initBp():
    if USB > 300:
        bp.color ="yellow"
        bp.accessories ="usb"
    else:
        bp.color ="red"
        bp.scaling = 0.9

    print(bp.color)
    print(bp.accessories)
    print(bp.scaling)

def initB():
    b.head = bp
    print(b.head.color)

def main():
    initBp()
    initB()
    resetBp()




if __name__=="__main__":
    main()

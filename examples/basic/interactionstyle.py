'''
Scene interaction styles. Available styles are:
      - 0, TrackballCamera
      - 1, TrackballActor
      - 2, JoystickCamera
      - 3, Unicam
      - 4, Flight
      - 5, RubberBand3D
      - 6, RubberBandZoom
'''
print(__doc__)
from vtkplotter import *

show([Sphere(), Cube()], at=[0, 1], shape=(3,1), bg='blackboard')

t = Text('''TrackballCamera is the default
...lets change it to JoystickCamera:''', c='k', bg='w')

print('..change it to JoystickCamera')
show([Paraboloid(), t], at=2, interactorStyle=2)

from graphics.rectangle import area,perimeter
l=10
b=5
print("Rectangle Area: ",area(l,b))
print("Rectangle perimeter:",perimeter(l,b))

import graphics.circle
r=7

print("circle Area: ",graphics.circle.area(r))
print("circle Perimeter: ",graphics.circle.perimeter(r))

import graphics.threed.cuboid as c
l=4
b=4
h=2

print("cuboid Area: ",c.area(l,b,h))
print("cuboid perimeter",c.perimeter(l,b,h))

from graphics.threed.sphere import area as sphere_area
from graphics.threed.sphere import perimeter as sphere_peri
r=5
print("Sphere Area: ",sphere_area(r))
print("Sphere perimeter: ",sphere_peri(r))
 

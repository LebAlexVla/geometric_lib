# Geometric library
## Description
**Functions for calculating the area and perimeter of geometric figures in _Python_**
## Functions
### Circle
#### area(r)
Returns the area of a circle with a given radius  
```python
r = input()
print(area(r))
```
input:
> 5

output:
> 78,5

#### perimeter(r)
Returns the perimeter of a circle with a given radius  
```python
r = input()
print(perimeter(r))
```
input:
> 5

output:
> 31,4


### Parallelogram
#### area(a, h)
Returns the area of a parallelogram with a given base and height  
```python
a = input()
h = input()
print(area(a, h))
```
input:
> 5 3

output:
> 15

#### perimeter(a, b)
Returns the perimeter of a parallelogram with given sides  
```python
a = input()
b = input()
print(perimeter(a, b))
```
input:
> 5 10

output:
> 30


### Square
#### area(a)
Returns the area of a square with a given side  
```python
a = input()
print(area(a))
```
input:
> 5

output:
> 25

#### perimeter(a)
Returns the perimeter of a square with a given side  
```python
a = input()
print(perimeter(a))
```
input:
> 5

output:
> 20


### Trapezoid
#### area(a, b, h)
Returns the area of a trapezoid with given bases and height  
```python
a = input()
b = input()
h = input()
print(area(a, b, h))
```
input:
> 5 7 4

output:
> 24

#### perimeter(a, b, c, d)
Returns the perimeter of a trapezoid with given sides and bases  
```python
a = input()
b = input()
c = input()
d = input()
print(perimeter(a, b, c, d))
```
input:
> 5 8 6 10

output:
> 29



## History of changes
### branch main
##### commit 8ba9aeb
> Circle and square added
##### commit d078c8d
> Docs added
##### commit d080c78
> Triangle added
##### commit 51c40eb
> Doc updated for triangle
##### commit d76db2a
> Add calculate.py
##### commit b5b0fae
> Update docs for calculate.py
##### commit 3049431
> Add rectangle.py
##### commit 6adb962
> Docs added
##### commit 438b89a
> Add user agreement
##### commit 86edb1c
> Update Docs. Add user agreement info
### branch new_feature_466480
##### commit a50b09b
> add parallelogram
##### commit 1d6b688
> add trapezoid
##### commit 4ad3c31
> correct parallelogram
##### commit fdd9321
> add comments

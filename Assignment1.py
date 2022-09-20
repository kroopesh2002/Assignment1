#Lists : A list is a collection datatype in which elements are ordered, changeable and also allow duplicate values.
#example of List is
fruit=['Apple','Banana','Orange','Apple','Pineapple']
print(fruit)
#adding an element to the list
fruit.append('pear')
print(fruit)
fruit.insert(3,'Mosambi')
print(fruit)
fruit.remove('mosambi')
print(fruit)
#slicing
print(fruit[1:3])
print(fruit[-4:-1])

#tuples: A tuple is a collection of elements which are ordered and unchangeable.
fruit=('Apple','Banana','Orange','Apple','Pineapple)
#slicing
print(fruit[0:2])
print(fruit[-5:-2])

#Dictionary: A Dictonary is a collection which is ordered, changeable and doesn't allow duplicates.
car={'brand':'Tata','model':'Safari','Price':'10 lakhs'}
print(car)
car.update('brand':'Mahindra')
print(car)
car.update('model':'xuv500')
print(car)
car.pop('Price')
print(car)
car.clear()
print(car)
del car
print(car)


#slicing in Dictionary
car={'brand':'Tata','model':'Safari','Price':'10 lakhs'}
print(car)
slicing=['brand','model']
slice_car={key:car[key] for key in slicing}
print(slice_car)
slicing=['Price']
slice_car={key:car[key] for key in slicing}
print(slice_car)

OUTPUT:
['Apple', 'Banana', 'Orange', 'Apple', 'Pineapple']
['Apple', 'Banana', 'Orange', 'Apple', 'Pineapple', 'pear']
['Apple', 'Banana', 'Orange', 'Mosambi', 'Apple', 'Pineapple', 'pear']
['Apple', 'Banana', 'Orange', 'Apple', 'Pineapple', 'pear']
['Banana', 'Orange']
['Orange', 'Apple', 'Pineapple']

('Apple', 'Banana')
('Apple', 'Banana', 'Orange')

{'brand': 'Tata', 'model': 'Safari', 'Price': '10 lakhs'}
{'brand': 'Mahindra', 'model': 'Safari', 'Price': '10 lakhs'}
{'brand': 'Mahindra', 'model': 'xuv500', 'Price': '10 lakhs'}
{'brand': 'Mahindra', 'model': 'xuv500'}
{}

{'brand': 'Tata', 'model': 'Safari', 'Price': '10 lakhs'}
{'brand': 'Tata', 'model': 'Safari'}
{'Price': '10 lakhs'}       

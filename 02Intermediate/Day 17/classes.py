# Creating our own classes in Python
class MyFirstPythonClass:  # Class names are in Pascal case (first letter of every word in caps)
    # pass  # "pass" keyword tells Python interpreter to skip the rest of the class - used for empty classes/functions

    # def __init__(self):  # constructor - there can only be ONE constructor in Python. No overloading constructors.
    #     self.class_attribute_for_all = "common attribute"  # This attribute will be available to all objects
    #     # "self" is like "this" keyword - syntax:  self[dot]<attribute name> = <attribute value>

    def __init__(self, parameter_value):  # Parameterized constructor
        self.class_attribute_01 = parameter_value
        self.class_attribute_02 = 0  # Can initialize an attribute in constructor with a default value

    def change_attribute_value(self, new_parameter_value):
        self.class_attribute_02 = new_parameter_value


my_class_object = MyFirstPythonClass("object 1")
# Adding object attributes - these are attributes of the object, not class.
# So another object of the same class will not have these attributes
my_class_object.object_attribute = "Object Attribute01"
print(my_class_object.object_attribute)

another_class_obj = MyFirstPythonClass("object 2")  # another_class_obj will not have the attributes "object_attribute"
print(another_class_obj.class_attribute_01)
print(another_class_obj.class_attribute_02)
another_class_obj.change_attribute_value("new value")
print(another_class_obj.class_attribute_01)
print(another_class_obj.class_attribute_02)

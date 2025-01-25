
# MOCKUP OF A DISTRIBUTION SYSTEM 

Company MockUp testing

# Created based on three partitions:

## 1. Area.py 

This code is a Python script that defines a class called areas which is used to manage different areas of a company. The class has several attributes and methods to add, remove, and retrieve users from different areas.

The __init__ method is the constructor for the class and it initializes the attributes maxDesarrolladores, maxDiseno, maxMarketing, and maxContabilidad based on the arguments passed to it.

The obtenerDatosArea method takes an area argument and returns the list of users in that area.

The registrarUsuario method takes a usuario object and an area argument and adds the user to the corresponding area if there are available spots. It returns 1 if the user was successfully added, -1 if there are no available spots in the area, and 0 if the area does not exist.

The consultarDisponibles method takes an area argument and returns the number of available spots in that area.

The eliminarUsuario method takes an idUsuario and an area argument and removes the user with the given ID from the corresponding area. It returns 1 if the user was successfully removed, -1 if the user does not exist in the area, and 0 if the area does not exist.

Overall, this code provides a way to manage different areas of a company and add/remove users from those areas based on availability.

## 2. Usario.py

This code defines a class called usuario with attributes for id, nombre, apellido, cedula, telefono, oficina, and sede. It also includes an __init__ method to initialize these attributes, a toString method to return a formatted string representation of the object, and getter methods for each attribute.



## 3. Cliente.py

This code is a Python program that simulates a system for managing user registrations and departments in a company. The program uses a class called areas to manage the departments and a class called usuario to manage the users.

The registrar_usuario function is used to register a new user. It prompts the user to input their name, last name, ID, phone number, office, and department. It then creates a new usuario object with the provided information and checks if the department has available spaces. If there are available spaces, it adds the user to the department and displays a success message. If there are no available spaces, it displays an error message.

The consultar_area function is used to display the available spaces in a department. It prompts the user to select a department and displays the available spaces in that department.

The dar_de_baja function is used to remove a user from a department. It prompts the user to input the user's ID and the department they belong to. It then removes the user from the department and displays a success message if the removal is successful. If the user is not found in the specified department, it displays an error message.

The main_menu function is the main interface of the program. It creates an instance of the areas class and displays a menu with options to select a department, register a user, remove a user, and exit the program.

To use this code, you can copy and paste it into a Python environment and run it.


## Why ?

This is a super simple Mockup for people to understand basic partitions of a whole distribution system, basically just for learning porpouse...

`KEEP ON LEARNING`



## 🚀 About Me
I'm a Site Reliability Engineer currently exploring hybrid Cloud world... And no... this is not just copy paste...


## Feedback

If you have any feedback, please reach out to me wander.tulo.jimenez@gmail.com


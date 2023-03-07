![](/assets/images/hbnb_logo.png)

This project is a simple copy of the [AirBnB Website](://intranet.alxswe.com/rltoken/m8g02HcD2ovrl_K-zulYBw).

The complete project is composed of the following:
* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
*  A website (the front-end) that shows the final product to everybody: static and dynamic
*  A database or files that store data (data = objects)
*  An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

# Final Product
![](/assets/images/hbnb_final_product_1.png)
![](/assets/images/hbnb_final_product_2.png)

# Project Breakdown

## The Console
* Data model
* Data management
    * Create
    * Update
    * Destroy
## The Command Interpreter
The command interpreter manages objects contained in the project, namely by:
* Creating new objects (eg: a new User or a new Place)
* Retrieving an object from a file, a database etc..
* Performing operations on objects (count, compute stats, et..)
* Updating attributes of an object
* Destroying/Deleting an object

# Directions



## Web Static

## MySQL Storage

## Web Framework

## RESTful API

## Web Dynamic

## Files and Directories
 * **`models`** directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
 * **`tests`** directory will contain all unit tests.
 * **`console.py`** file is the entry point of our command interpreter.
 * **`models/base_model.py`** file is the base class of all our models. It contains common elements:
     * attributes: **`id, created_at`** and **`updated_at`**
     * methods: **`save()`** and **`to_json()`**
 * **`models/engine`** directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py

 ## Storage Principales

 ### 1. Storing an Instance

 ### 2. File Storage via JSON

 ## Database Structure
 ![](/assets/images/data_diagram.jpg)

 # AUTHORS
* Siphelele Makhathini <siphelele.mlungisi@gmail.com>
* Lorenzo Lawrence <jerumehlawrence@gmail.com>

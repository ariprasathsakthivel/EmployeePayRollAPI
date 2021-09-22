'''
@Author: Ariprasath
@Date: 2021-09-21 19:00:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-22
@Title : API for processing HTTP methods(CRUD operations)
'''

from flask import Flask, app, request, jsonify
import random


app=Flask(__name__)

employees=list()

def company_emp_wage():
    '''
    Description:
        Calculates the wage and attendence of a given employee
    Parameters:
        None
    Returns:
        attendence,wage(tuple): Both attendence and wage will be returened as a tuple. 
    '''
    attend=random.randint(0,2)
    if attend==0:
        attendence="Absent"
        wage=0
        return attendence,wage
    elif attend==1:
        attendence="Half day present"
        wage=80
        return attendence,wage
    elif attend==2:
        attendence="Full day present"
        wage=160
        return attendence,wage



@app.get("/Employees")
def get_employees():
    '''
    Descrition:
        Checks the length of the list employees and returns all the elements of the list in the json format 
    Parameters:
        None
    Returns:
        returns all the elements of the list in the json format if the length of the employees list greater than zero
    '''
    if len(employees)>0:
        return jsonify(employees)
    return jsonify({"message":"There are no employees"})

@app.get("/Employees/<string:name>")
def get_employee(name):
    '''
    Description:
        Checks the length of the list employees and returns the given employee details in the json format
    Parameters:
        name(string): Name of the employee
    Returns:
        returns the given employee details in the json format if the length of the employees list is greater than zero and the employee name is present in the employees list
    '''
    if len(employees)>0:
        flag=0
        for element in employees:
            if element["Employee name"]==name:
                flag=1
                return jsonify(element)
        if flag!=1:
            return jsonify({"message":"The given employer is not present"})
    return jsonify({"message":"There are no employees"})

@app.post("/Employees")
def create_employees():
    '''
    Description:
        Creates a new employee data that contains the employees name, attendence and wage
    Parameter:
        None
    Returns:
        The newly created employee details in the json format
    '''
    data=company_emp_wage()
    emp_name=request.get_json()
    employee=dict()
    employee["Employee name"]=emp_name["name"]
    employee["Attendence"]=data[0]  
    employee["Wage"]=data[1]
    employees.append(employee)
    return jsonify(employee)

@app.put("/Employees/<string:name>")
def update_employees(name):
    '''
    Description:
        Updates the complete details of a particular employee
    Parameter:
        name(string): Name of the employee 
    Retunrs:
        All updated detials of the employee in the json format
    '''
    update_data=request.get_json()
    flag=0
    for element in employees:
        if element["Employee name"]==name:
            element["Employee name"]=update_data["Employee name"]
            element["Attendence"]=update_data["Attendence"]
            element["Wage"]=update_data["Wage"]
            flag=1
            return jsonify(element)
    if flag!=1:
        return jsonify({"message":"The given employer is not present"})
        


@app.delete("/Employees/<string:name>")
def delete_employee(name):
    '''
    Description:
        Deletes all the details of a particular employee
    Parameter:
        name(string): Name of the employee
    Returns:
        An empty json data
    '''
    flag=0
    for element in employees:
        if element["Employee name"]==name:
            employees.pop(employees.index(element))
            flag=1
            return jsonify({})
    if flag!=1:
        return jsonify({"message":"The given employer is not present"})

@app.patch("/Employees/<string:name>/Employee_name")
def update_employee_name(name):
    '''
    Description:
        Updates the name of the employee
    Parameters:
        name(string): The existing name of the employee
    Returns:
        Complete details of an employee with updated name
    '''
    flag=0
    data=request.get_json()
    for element in employees:
        if element["Employee name"]==name:
            element["Employee name"]=data["name"]
            flag=1
            return jsonify(element)
    if flag!=1:
        return jsonify({"message":"The given employer is not present"})

@app.patch("/Employees/<string:name>/Attendence")
def update_employee_attendence(name):
    '''
    Description:
        Updates the attendence of the employee
    Parameters:
        name(string): The existing name of the employee
    Returns:
        Complete details of an employee with updated attendence
    '''
    flag=0
    data=request.get_json()
    for element in employees:
        if element["Employee name"]==name:
            element["Attendence"]=data["Attendence"]
            flag=1
            return jsonify(element)
    if flag!=1:
        return jsonify({"message":"The given employer is not present"})

@app.patch("/Employees/<string:name>/Wage")
def update_employee_wage(name):
    '''
    Description:
        Updates the wage of the employee
    Parameters:
        name(string): The existing name of the employee
    Returns:
        Complete details of an employee with updated wage
    '''
    flag=0
    data=request.get_json()
    for element in employees:
        if element["Employee name"]==name:
            element["Wage"]=data["Wage"]
            flag=1
            return jsonify(element)
    if flag!=1:
        return jsonify({"message":"The given employer is not present"})

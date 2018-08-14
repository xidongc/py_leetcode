"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emp = {employee.id : employee for employee in employees}
        return self.helper(emp, id)
    def helper(self, emp, id):
        res = sum(self.helper(emp,employeeId) for employeeId in emp[id].subordinates)
        return res + emp[id].importance
        
# sum(iterable including list, tuple, set, without [] is fine)
# sum([]) = 0?
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
Output: 11

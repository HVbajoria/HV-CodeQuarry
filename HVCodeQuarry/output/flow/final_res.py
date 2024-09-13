
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str, input2:str, input3: str, input4:str) -> str:
    return 'Question ' + input1 + 'Sample Testcases' + input2 + 'Code' + input3 + 'Testcase Gen' + input4
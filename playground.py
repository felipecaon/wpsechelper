from prettytable import PrettyTable

ADMIN_ACTIONS_DATA = ['Action Name', 'Function', 'File']
ADMIN_ACTIONS_DATA.append(["a", "b", "x"])

table = PrettyTable(ADMIN_ACTIONS_DATA)
print(table)

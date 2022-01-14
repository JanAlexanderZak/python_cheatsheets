import sys
import subprocess
print(sys.executable)

args = sys.argv
if len(args) != 1:
    exit()
else:
    for argument in sys.argv:
        print(argument)
    arg = str(args[0])

print("Builtin modules: ", sys.builtin_module_names)

# Subprocess
result = subprocess.run("pwd", capture_output=True)
print(result)

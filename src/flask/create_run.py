import glob
import os

IMPORT_FLG   = "#route_import\n"
REGISTER_FLG = "#route_register\n"


def create_run():
    file_str = ""
    files = glob.glob(os.path.dirname(__file__) + '/route/*.py')
    print(files)
    file_names = []
    for file in files:
        file_split = file.split('/')
        file_name = file_split[-1]
        file_name = file_name.replace('.py','')
        file_names.append(file_name)
    with open(os.path.dirname(__file__) +'/run_template') as f:
        for line in f.readlines():
            file_str += line
            if line == IMPORT_FLG:
                for file in file_names:
                    file_str += "from route import " + file + "\n"
            if line == REGISTER_FLG:
                for file in file_names:
                    file_str += "app.register_blueprint(" + file + ".bp)\n"
                    
                    

    with open(os.path.dirname(__file__) + '/run.py', 'w') as f:
        f.write(file_str)

if __name__ == "__main__":
    create_run()
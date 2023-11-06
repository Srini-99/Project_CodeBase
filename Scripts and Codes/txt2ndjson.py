import json

relations = {1: "vfork", 2: "clone", 3: "execve", 4: "kill", 5: "pipe", 6: "delete", 7: "create", 8: "recv", 9: "send", 10: "mkdir", 11: "rmdir", 12: "open", 13: "load", 14: "read", 15: "write", 16: "connect", 17: "getpeername", 18: "filepath", 19: "mode", 20: "mtime", 21: "linknum", 22: "uid", 23: "count", 24: "nametype", 25: "version", 26: "dev", 27: "sizebyte", 28: "edgetype_num"}
types = {1: "process", 2: "file", 3: "socket"}

def parse_edgefact(input_file, output_file):

    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            
            fields = line.strip().split()

            if len(fields) < 7:
                fields.extend(['NULL'] * (7 - len(fields)))  # Fill missing fields with 'NULL'
            
            null_count = fields.count('NULL')

            if null_count<=1:
                json_dict = {
                    'e_id': fields[0],
                    'n1_hash': fields[1],
                    'n2_hash': fields[2],
                    'relation': relations[int(fields[3])],
                    'sequence': fields[4],
                    'session': fields[5],
                    'timestamp': fields[6]
                }
            else:
                json_dict = {}
            
            if json_dict:
                json_str = json.dumps(json_dict)
                f_out.write(json_str + "\n")

def parse_procfact(input_file, output_file):

    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            
            fields = line.strip().split()

            if len(fields) < 5:
                fields.extend(['NULL'] * (5 - len(fields)))  # Fill missing fields with 'NULL'

            null_count = fields.count('NULL')

            if null_count<=1:
                id_value = fields[0]
                pid = fields[1]
                exe = ""
                ppid = ""
                args = []

                # Loop through fields to correctly identify exe and ppid
                for i, field in enumerate(fields[2:]):
                    if field.isnumeric() and not ppid:
                        ppid = field
                    elif not ppid:
                        exe += " " + field
                    else:
                        args.append(field)

                exe = exe.strip()

                json_dict = {
                    "id": id_value,
                    "pid": pid,
                    "exe": exe,
                    "ppid": ppid,
                    "args": " ".join(args)
                }
            else:
                json_dict = {}
            
            if json_dict:
                json_str = json.dumps(json_dict)
                f_out.write(json_str + "\n")
            
def parse_nodefact(input_file, output_file):

    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            
            fields = line.strip().split()

            if len(fields) < 2:
                fields.extend(['NULL'] * (2 - len(fields)))  # Fill missing fields with 'NULL'
            
            null_count = fields.count('NULL')

            if null_count<1:
                json_dict = {
                    'id': fields[0],
                    'type': types[int(fields[1])]
                }
            else:
                json_dict = {}
            
            if json_dict:
                json_str = json.dumps(json_dict)
                f_out.write(json_str + "\n")

def parse_socketfact(input_file, output_file):

    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            
            fields = line.strip().split()

            if len(fields) < 2:
                fields.extend(['NULL'] * (2 - len(fields)))  # Fill missing fields with 'NULL'

            null_count = fields.count('NULL')

            if null_count<1:
                json_dict = {
                    'id': fields[0],
                    'name': fields[1]
                }
            else:
                json_dict = {}
            
            if json_dict:
                json_str = json.dumps(json_dict)
                f_out.write(json_str + "\n")

def parse_filefact(input_file, output_file):

    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            
            fields = line.strip().split()

            if len(fields) < 3:
                fields.extend(['NULL'] * (3 - len(fields)))  # Fill missing fields with 'NULL'

            null_count = fields.count('NULL')

            if null_count<=1:
                json_dict = {
                    'id': fields[0],
                    'name': fields[1],
                    'version': fields[2]
                }
            else:
                json_dict = {}
            
            if json_dict:
                json_str = json.dumps(json_dict)
                f_out.write(json_str + "\n")

if __name__ == "__main__":
    proc = 'procfact.txt'
    op_proc = 'procfact.ndjson'

    edge = 'edgefact_0.txt'
    op_edge = 'edgefact_0.ndjson'   

    filef = 'filefact.txt'
    op_file = 'filefact.ndjson'

    sock = 'socketfact.txt'
    op_sock = 'socketfact.ndjson'

    node = 'nodefact.txt'
    op_node = 'nodefact.ndjson'
    
    parse_procfact(proc, op_proc)
    parse_edgefact(edge, op_edge)
    parse_filefact(filef, op_file)
    parse_socketfact(sock, op_sock)
    parse_nodefact(node, op_node)

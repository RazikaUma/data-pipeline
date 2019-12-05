import util

input_path = 'elb_log_file.txt'
output_path = 'anonymized_data.txt'
o_f = open(output_path, "w+")
with open(input_path) as fp:
   line = fp.readline()
   record = ""
   while line:
       stripped_line = line.strip()
       if line == "\n":
           parsed_line = util.parse_line(record)
           if len(parsed_line) > 0:
               o_f.write(parsed_line)
               o_f.write('\n')
               record =""
       else:
           record = record + " " + stripped_line
       line = fp.readline()

o_f.close()
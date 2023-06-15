import re

raw_log_file = '/Users/suchitbaniya/Desktop/system/raw_log.txt'

with open(raw_log_file,'r') as file:
    for line in file:
        
        match = re.match(r'(.*?)\s(\d+\.\d+\.\d+\.\d+)', line)
        if match:
            host = match.group(1)
            ip_address = match.group(2)

            
            ip_parts = ip_address.split('.')
            ip_file_name = '.'.join(ip_parts[:-1])
            ip_write_here = '-'.join(ip_parts)

            file_name1 = f'FILE.{ip_file_name}'
            file_name2 = f'{ip_write_here}-write-here'

            
            with open(file_name1, 'a') as file1:
                file1.write(f'{host} {ip_address}\n')

            with open(file_name2, 'a') as file2:
                file2.write(f'{host} {ip_address}\n')

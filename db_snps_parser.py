import sys
import vcf

def filter_vcf_with_1000genomes(input_vcf_file, output_vcf_file):
    d = {}

    vcf_reader = vcf.Reader(open(input_vcf_file, 'r'))
    vcf_writer = vcf.Writer(open(output_vcf_file, 'w'), vcf_reader)

    for record in vcf_reader:
        rsid = record.ID
        if 'FREQ' in record.INFO.keys():
            info = record.INFO['FREQ']
            info_str = ','.join([item if item is not None else '.' for item in info])
            parts = info_str.split('|')
            for part in parts:
                key_value = part.split(':')
                key = key_value[0]
                values = key_value[1].split(',')
                values = [float(x) for x in values if x != '.']
                sorted_values = sorted(values,reverse=True)
                rsid_db = '_'.join([rsid,key])
                #if rsid in d:
                    #d[rsid_db].append(tuple(map(str,values)))
                d[rsid_db] = sorted_values[1]
                #else:
                #    val = []
                #    val.append(tuple(map(str,values)))
                #    d[rsid_db] = val
    return(d)

    #vcf_writer.close()

# Replace 'input.vcf' and 'output.vcf' with your input and output file paths.
input_file_path = 'test.vcf'
output_file_path = 'output.vcf'

d = filter_vcf_with_1000genomes(input_file_path, output_file_path)

for k,v in d.items():
	print(k,v)


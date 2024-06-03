import argparse
import json
import os

def convert_json_to_jsonl(input_file, output_file):
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    with open(output_file, 'w') as outfile:
        for item in data:
            json_line = json.dumps(item)
            outfile.write(json_line + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON file to JSONL format.")
    parser.add_argument('--input_file', type=str, required=True, help='Input JSON file name')
    parser.add_argument('--output_file', type=str, required=True, help='Output JSONL file name')
    
    args = parser.parse_args()
    
    convert_json_to_jsonl(args.input_file, args.output_file)


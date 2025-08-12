import sys
import codecs

def convert_encoding(input_path, output_path, input_encoding, output_encoding):
    """
    指定されたエンコーディングでファイルを読み込み、別のエンコーディングで書き出す
    """
    try:
        with codecs.open(input_path, 'r', input_encoding) as f_in:
            content = f_in.read()
        with codecs.open(output_path, 'w', output_encoding) as f_out:
            f_out.write(content)
        print(f"Successfully converted {input_path} ({input_encoding}) to {output_path} ({output_encoding})")
    except Exception as e:
        print(f"Error converting file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python convert.py <input_path> <output_path> <input_encoding> <output_encoding>", file=sys.stderr)
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    input_encoding = sys.argv[3]
    output_encoding = sys.argv[4]
    
    convert_encoding(input_path, output_path, input_encoding, output_encoding)
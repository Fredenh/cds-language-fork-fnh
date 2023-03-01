import argparse

def input_parse():
    # initialize the parser
    parser = argparse.ArgumentParser()
    # add arguments // "--name" is what you feed it in the command line
    parser.add_argument("--name", type=str, default="Frederik")
    parser.add_argument("--age", type=int)
    # parse the arguments from command line
    args = parser.parse_args()
    return args

def hello(name, age):
    print("Hello, my name is " + name + "!")
    print("I am " + str(age) + " years old!") # putting () around age because its an int and therefore conflicts the string of name

def main():
    # run input parse to get name
    args = input_parse()
    # pass name to hello()
    hello(args.name, args.age)

if __name__=="__main__": #if this .py script is called from command line, i want you to run the main function
main()

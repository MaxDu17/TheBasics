import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--test",
    type = str,
    default = "Clark",
    required = False, # you can require an argument
    help = "add help here"
)

args = parser.parse_args()
print(args.test)

# run this as argparse_demo.py --test bob      -> should print out "bob"
# run this as argparse_demo.py      -> should print out "clark"
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--test",
    type = str,
    default = "Clark",
    required = False, # you can require an argument
    help = "add help here"
)

parser.add_argument(
    "--direct_flag",
    action="store_true", # means that you store direct_flag = true if we use this flag
    help = "add help here"
)

args = parser.parse_args()
print(args.test)
print(args.direct_flag)

# run this as argparse_demo.py --test bob      -> should print out "bob" / False
# run this as argparse_demo.py      -> should print out "clark" / False
# run this as argparse_demo.py --test bob --direct_flag         -> should print out "bob" / True

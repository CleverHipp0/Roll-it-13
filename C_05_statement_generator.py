def statement_generator(decoration, decoration_time, statement):
    """Makes a statement fancy by adding decorative characters"""

    print(f"{decoration * decoration_time} {statement} {decoration * decoration_time}")


deco = input("d: ")
deco_time = int(input("dt: "))
state = input("s: ")

statement_generator(deco, deco_time, state)


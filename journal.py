import os


def load(name):
    filepath = get_filepath(name)
    jnal = []
    if os.path.exists(filepath):
        print("Loading from {}".format(filepath))
        with open(filepath) as fin:
            for entry in fin.readlines():
                jnal.append(entry.rstrip())
    return jnal


def save(name, jnal):
    filepath = get_filepath(name)
    print("Saving to {}".format(filepath))
    with open(filepath, 'w') as fout:
        for entry in jnal:
            fout.write(entry + '\n')
    return


def get_filepath(name):
    filepath = os.path.abspath(os.path.join('.', 'journals', name + '.jnl'))
    return filepath


def add_entry(entry, jnal):
    jnal.append(entry)
    return

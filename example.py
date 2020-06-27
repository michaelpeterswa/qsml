import qsml
import pprint

pp = pprint.PrettyPrinter(indent=4)

file = "example.qsml"

retval = qsml.load(file)

retval["myportfolio"].update({"NWST": "12"})

qsml.dump("output.qsml", retval)

pp.pprint(retval)

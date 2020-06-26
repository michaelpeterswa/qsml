import qsml
import pprint

pp = pprint.PrettyPrinter(indent=4)

file = "example.qsml"

pp.pprint(qsml.load(file))

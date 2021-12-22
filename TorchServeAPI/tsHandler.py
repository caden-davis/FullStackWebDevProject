import tsHandlerDef as handler

import sys
data = sys.argv[1]
context = sys.argv[2]

print(handler.handle(data, context))
import json_process
import files_load

jsons = files_load.all_load('json/release/')
test=json_process.jsons_process(jsons,["published_at"])
print(test)

address = {}
address["Riya"]={
    'name' : 'Riya',
    'address' : '90, micmac crescent, North york, ON M2H 2K2',
    'mobileno' : 6478713858
}
address["Krupali"]={
    'name' : 'krupali',
    'address' : '90, micmac crescent, North york, ON M2H 2K2',
    'mobileno' : 4324322323
}
import json
s = json.dumps(address)
print(s)
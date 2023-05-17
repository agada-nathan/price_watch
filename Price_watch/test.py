
vendor_ids = []

with open('business_names.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line != '':
            vendor = line.split(':')
            vendor_ids.append(vendor[1])
        
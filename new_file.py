import csv

with open('scrape_file.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)

    with open('names.csv','w') as new_names:
        field_names=['title','content']

        csv_writer=csv.DictWriter(new_names,fieldnames=field_names,delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)

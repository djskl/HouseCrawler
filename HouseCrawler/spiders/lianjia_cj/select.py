src_file = "/root/20180325_cj_lj.csv"

with open("/root/2017.csv", "w") as writer:
    with open(src_file) as reader:
        header = reader.readline()
        writer.write(header)
        for line in reader:
            fields = line.split(",")
            dates = fields[4].split(".")

            if len(dates) < 2:
                continue

            year = int(dates[0])
            if year > 2016:
                writer.write(line)
if __name__ == "__main__":
    with open('src/data/adsl_tci.txt', 'r') as firstfile, open('output/ir_domains.txt', 'w') as secondfile:

        # read content from first file
        for line in firstfile:
            # write content to second file
            secondfile.write(line)
           

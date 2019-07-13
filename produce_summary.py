# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip().split('|')
    
#     melon = line[0]
#     count = line[1]
#     amount = line[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


def melon_count_summary(day_number, path):
    """Given the day and file path, give the summary of what was sold on that day"""
    print("Day", day_number)
    the_file = open(path)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        print("Delivered {} {}s for total of ${}".format(words[1], words[0], words[2]))
    the_file.close() 

print(melon_count_summary(1, "um-deliveries-20140519.txt"))
print(melon_count_summary(2, "um-deliveries-20140520.txt"))
print(melon_count_summary(3, "um-deliveries-20140521.txt"))





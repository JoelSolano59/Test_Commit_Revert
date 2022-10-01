def Add(s):
    # Add implementation
    if s == "":
        return 0
    else:
        res = 0
        lines = s.split("\n")
        for line in lines:
            nums = line.split(",")
            for num in nums:
                res += int(num)
        return res

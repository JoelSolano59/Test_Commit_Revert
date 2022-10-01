def Add(s):
    # Add implementation
    if s == "":
        return 0
    else:
        nums = s.split(",")
        res = 0
        for num in nums:
            res += int(num)
        return res

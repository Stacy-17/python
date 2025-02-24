def find_needle(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    else:
        return haystack.find(needle)

# example

haystack="I found a dog jumping and the dog started running"
needle="dog"
print(find_needle(haystack,needle))

nums=[1,2,2,3,3,4,4,4,5,5,6,7,7,7,7,8,8,9,9,10,80,70,77,77,67,8,9]
print(nums)
print(set(nums))
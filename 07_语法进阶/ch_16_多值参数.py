def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)


demo(1) # 输出：1 () {}
demo(1, 2, 3, 4, 5) # 输出：1, (2, 3, 4, 5) {}
demo(1, 2, 3, 4, 5, name="小明", age=18)    # 输出：1, (2,3,4,5) {name="小明",age=18}
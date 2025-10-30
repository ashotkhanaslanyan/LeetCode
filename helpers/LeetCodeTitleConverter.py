leetcode_title: str = input("Enter the LeetCode title: ")
leetcode_title = leetcode_title.replace(".", "").replace(" ", "_").lower()
print(f"problem_{leetcode_title}/solution.py")

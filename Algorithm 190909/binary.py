class Tree:
    def __init__(self, me, left, right):
        self.me = me
        self.left = left
        self.right = right
        self.visit = 0


def make(tree):
    if tree.visit == 0:
        tree.left = Tree(tree.me + 1, 0, 0)
        make(tree.left)
        tree.visit = 1
        tree.right = Tree(tree.left.me + 1)
        make(tree.right)


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    children = [0] * (N + 1)
    visit = [0] * (N + 1)
    t = Tree(1, 0, 0)
    print(t.me, t.left, t.right)
    # getlist = make(t)
    # root, half = find(getlist, N)
    # print("#{} {} {}".format(tc, root, half))

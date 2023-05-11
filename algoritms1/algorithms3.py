class mySet:
    def __init__(self):
        self.set_size = 10
        self.my_set = [[] for _ in range(self.set_size)]

    def add(self, x):
        self.my_set[x % self.set_size].append(x)

    def find(self, x):
        for now in self.my_set[x % self.set_size]:
            if now == x:
                return True

        return False

    def delete(self, x):
        x_list = self.my_set[x % self.set_size]
        for i in range(len(x_list)):
            if x_list[i] == x:
                x_list[i] = x_list[len(x_list) - 1]
                x_list.pop()
                return


if __name__ == '__main__':
    solution = mySet()
    solution.add(x=14)
    solution.add(24)
    solution.add(4)
    solution.delete(24)
    print(solution.find(24))

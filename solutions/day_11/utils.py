class Monkey:
    def __init__(
        self,
        monkey_index,
        items=[],
        operation="",
        test=1,
        monkey_truthy_test_case=0,
        monkey_falsy_test_case=0,
    ):
        self.monkey_index = monkey_index
        self.items = items
        self.operation = operation
        self.test = test
        self.monkey_truthy_test_case = monkey_truthy_test_case
        self.monkey_falsy_test_case = monkey_falsy_test_case
        self.inspected_items = 0

    def evaluate_operation(self, item):
        old = item
        return eval(self.operation)

    def __repr__(self) -> str:
        return str(self.items)


def create_monkeys(monkeys_description):
    monkey_index = 0
    monkeys = []

    for line in monkeys_description:
        line = line.replace(" ", "")
        if line.startswith("Monkey"):
            monkey = Monkey(monkey_index)
            monkey_index += 1
        if line.startswith("Startingitems:"):
            monkey.items = [
                int(item) for item in line.split("Startingitems:")[1].split(",")
            ]
        if line.startswith("Operation:new="):
            monkey.operation = line.split("Operation:new=")[1]
        if line.startswith("Test:divisibleby"):
            monkey.test = int(line.split("Test:divisibleby")[1])
        if line.startswith("Iftrue:throwtomonkey"):
            monkey.monkey_truthy_test_case = int(line.split("Iftrue:throwtomonkey")[1])
        if line.startswith("Iffalse:throwtomonkey"):
            monkey.monkey_falsy_test_case = int(line.split("Iffalse:throwtomonkey")[1])
            monkeys.append(monkey)
    return monkeys

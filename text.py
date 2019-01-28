sandwich_orders = ['wqd', 'dwq', 'qqq']
finished_sandwiches = []

while sandwich_orders:
    for sandwich_order in sandwich_orders:
        current_sandwiches = sandwich_orders.pop()
        # pop 后已经移动到current_sandwiches

        print("I made your " + current_sandwiches)
        finished_sandwiches.append(current_sandwiches)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

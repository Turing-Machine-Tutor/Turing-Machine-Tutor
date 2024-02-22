list=["f","u","c","k"]
tape_str = ' '.join(list)

head_position_str = ' ' * (2 * 0) + '^'

state_step_info = f"State: q0 | Step: {68 + 1}"


print(tape_str)
print(head_position_str)
print(state_step_info)
print('-' * (2 * len(list) + 1))  # Separator line
list.insert(0,"dd")
print(list)

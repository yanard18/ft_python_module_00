def ft_count_harvest_recursive():
	print_days_n_times(int(input("Days until harvest: ")))
	print("Harvest time!")

def print_days_n_times(max_val, current=1):
	if current <= max_val:
		print(f"Day {current}")
		print_days_n_times(max_val, current + 1)

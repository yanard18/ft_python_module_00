def ft_count_harvest_recursive():
    def count_days(max_val, current=1):
        if current <= max_val:
            print(f"Day {current}")
            count_days(max_val, current + 1)

    day = int(input("Days until harvest: "))
    count_days(day)
    print("Harvest time!")

def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Tower of Hanoi recursion.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)


if __name__ == "__main__":
    tower_of_hanoi(3, 'A', 'C', 'B')

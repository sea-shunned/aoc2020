with open("input.txt", "r") as f:
    boarding_passes = f.read().splitlines()

decoder = {
    "F": '0',
    "B": '1',
    "R": '1',
    "L": '0'
}

possible_seat_ids = []

for r in range(1, 127):
    for c in range(8):
        possible_seat_ids.append(r * 8 + c)

possible_seat_ids = set(possible_seat_ids)

for boarding_pass in boarding_passes:
    # Convert to binary and then an int
    row = int(''.join([decoder[i] for i in boarding_pass[:7]]), 2)
    col = int(''.join([decoder[i] for i in boarding_pass[7:]]), 2)

    seat_id = row * 8 + col

    possible_seat_ids.remove(seat_id)

print(possible_seat_ids)
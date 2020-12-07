with open("input.txt", "r") as f:
    boarding_passes = f.read().splitlines()

decoder = {
    "F": '0',
    "B": '1',
    "R": '1',
    "L": '0'
}

max_seat_id = 0

for boarding_pass in boarding_passes:
    # Convert to binary and then an int
    row = int(''.join([decoder[i] for i in boarding_pass[:7]]), 2)
    col = int(''.join([decoder[i] for i in boarding_pass[7:]]), 2)

    seat_id = row * 8 + col

    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)
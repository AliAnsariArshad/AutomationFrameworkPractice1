import moment

x = moment.now()
y = moment.now().strftime("%H-%M-%S_%d-%m-%Y")

print(x)
print(y)
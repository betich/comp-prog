u = list(map(float, input()[1:-1].split(',')))
v = list(map(float, input()[1:-1].split(',')))

ans = [u[0] + v[0], u[1] + v[1], u[2] + v[2]]

print(u, '+', v, '=', ans)

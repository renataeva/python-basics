
def exam(limit, marks):
    done = 0
    for i in marks:
        if i >= limit:
            done += 1
    return done


print(exam(3, [4, 1, 5, 2, 3, 3, 4]))
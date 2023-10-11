def gather_credits(credits, *args):
    courses = []
    current_credits = 0
    for name, course_credits in args:
        if name in courses:
            continue

        if current_credits >= credits:
            break

        courses.append(name)
        current_credits += course_credits

    if current_credits >= credits:
        res = f"Enrollment finished! Maximum credits: {current_credits}.\n" + f"Courses: {', '.join(sorted(courses))}\n"
        return res

    return f"You need to enroll in more courses! You have to gather {credits - current_credits} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

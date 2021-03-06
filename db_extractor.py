import sqlite3


def main():
    path = "tmp/apps/com.oceanwing.smarthome/db/EufyLifeDb.db"

    fields = ["id", "createtime", "weight", "bmr", "bodyfat", "bodyfatmass", "muscle", "musclemass", "bone", "bonemass",
              "leanbodymass", "visceralfat", "water", "proteinpercentage"]

    connection = sqlite3.connect(path)
    c = connection.cursor()

    query = "SELECT " + ("{}," * (len(fields) - 1) + "{}").format(*fields) + " from bodyfathistorym"
    response = c.execute(query).fetchall()

    csv_template = "{}," * (len(fields) - 1) + "{}\n"

    file = open("body_stats.csv", "w")
    file.write(csv_template.format(*fields))
    for row in response:
        file.write(csv_template.format(*row))


if __name__ == "__main__":
    main()
